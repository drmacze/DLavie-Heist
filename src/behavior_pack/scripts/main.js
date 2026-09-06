import {
  world,
  system,
  EquipmentSlot,
  EntityComponentTypes,
  InputPermissionCategory,
  EasingType,
} from "@minecraft/server";

const SAFE_ID = "dlv:vault_safe";
const CROWBAR_ID = "dlv:crowbar";
const MONEY_OBJECTIVE = "dlv_money";
const ACTIVE_TAG = "dlv_heist_active";
const HIDE_HUD_TAG = "dlv_hide_money_hud";
const TICKS_PER_SECOND = 20;

const sessions = new Map();
const reservedVaults = new Map();

function clamp(value, min, max) { return Math.min(max, Math.max(min, value)); }
function getVaultKey(dimensionId, location) { return `${dimensionId}:${Math.floor(location.x)},${Math.floor(location.y)},${Math.floor(location.z)}`; }
function safeMessage(player, message) { try { player.sendMessage(message); } catch {} }

function getMoneyObjective() {
  let objective = world.scoreboard.getObjective(MONEY_OBJECTIVE);
  if (!objective) objective = world.scoreboard.addObjective(MONEY_OBJECTIVE, "DLavie Money");
  return objective;
}
function getMoney(player) { try { return getMoneyObjective().getScore(player) ?? 0; } catch { return 0; } }
function addMoney(player, amount) {
  const objective = getMoneyObjective();
  const current = objective.getScore(player) ?? 0;
  objective.setScore(player, current + amount);
  return current + amount;
}
function isCrowbarEquipped(player) {
  try {
    const equippable = player.getComponent(EntityComponentTypes.Equippable);
    return equippable?.getEquipment(EquipmentSlot.Mainhand)?.typeId === CROWBAR_ID;
  } catch { return false; }
}
function setInputLocked(player, locked) {
  try { player.inputPermissions.setPermissionCategory(InputPermissionCategory.Movement, !locked); } catch {}
  try { player.inputPermissions.setPermissionCategory(InputPermissionCategory.Camera, !locked); } catch {}
}
function clearHeistCamera(player) {
  try { player.camera.clear(); } catch { try { player.camera.setDefaultCamera("minecraft:first_person"); } catch {} }
}
function recoverPlayer(player) {
  try {
    if (!player.hasTag(ACTIVE_TAG)) return;
    setInputLocked(player, false);
    clearHeistCamera(player);
    player.removeTag(ACTIVE_TAG);
    player.onScreenDisplay.setActionBar("");
  } catch {}
}
function squaredDistance(a, b) { const dx=a.x-b.x, dy=a.y-b.y, dz=a.z-b.z; return dx*dx+dy*dy+dz*dz; }
function getPlayerById(playerId) { for (const player of world.getPlayers()) if (player.id === playerId) return player; }

function cameraShot(player, center, phase) {
  const shots = [
    {x:center.x+3.2,y:center.y+2.0,z:center.z+3.1},
    {x:center.x-3.0,y:center.y+2.5,z:center.z+2.2},
    {x:center.x+2.1,y:center.y+3.8,z:center.z-3.4},
  ];
  const location = shots[clamp(phase,0,shots.length-1)];
  try {
    player.camera.setCamera("minecraft:free", {
      location,
      facingLocation:{x:center.x,y:center.y+0.55,z:center.z},
      easeOptions:{easeTime:0.75,easeType:EasingType.InOutCubic},
    });
  } catch { try { player.camera.setCamera("minecraft:third_person"); } catch {} }
}
function playPryAnimation(player) { try { player.playAnimation("animation.dlv.heist.pry", {blendOutTime:0.18}); } catch {} }
function emitHeistNoise(session, player) {
  try { player.playSound("random.anvil_land", {volume:0.55,pitch:1.35}); } catch {}
  try {
    system.sendScriptEvent("dlv:heist_noise", JSON.stringify({dimension:session.dimensionId,x:session.blockLocation.x,y:session.blockLocation.y,z:session.blockLocation.z,radius:18,playerId:session.playerId}));
  } catch {}
}
function formatProgress(progress, remainingSeconds) {
  const segments=20, filled=clamp(Math.floor(progress*segments),0,segments);
  return `§6VAULT BREACH  §f${Math.floor(progress*100)}%\n§a${"█".repeat(filled)}§7${"░".repeat(segments-filled)}  §f${remainingSeconds}s`;
}
function cleanupSession(session, reason, showMessage=true) {
  sessions.delete(session.playerId);
  reservedVaults.delete(session.vaultKey);
  const player=getPlayerById(session.playerId);
  if (!player) return;
  setInputLocked(player,false);
  clearHeistCamera(player);
  try { player.removeTag(ACTIVE_TAG); } catch {}
  try { player.onScreenDisplay.setActionBar(""); } catch {}
  if (showMessage && reason) safeMessage(player,`§c[DLavie Heist] ${reason}`);
}
function failSession(session, reason) { cleanupSession(session,reason,true); }

function finishSession(session, player, block) {
  try {
    if (block.permutation.getState("dlv:opened") === true) { cleanupSession(session,"Brankas sudah terbuka.",false); return; }
    block.setPermutation(block.permutation.withState("dlv:opened",true));
  } catch { failSession(session,"Brankas tidak dapat diselesaikan."); return; }
  let balance=0;
  try { balance=addMoney(player,session.reward); } catch { balance=getMoney(player); }
  try { player.playSound("random.levelup",{volume:0.9,pitch:1.1}); } catch {}
  try {
    player.onScreenDisplay.setTitle("§aHEIST SUCCESS",{subtitle:`§6+$${session.reward.toLocaleString()}  §8•  §fBalance $${balance.toLocaleString()}`,fadeInDuration:5,stayDuration:45,fadeOutDuration:12});
  } catch { safeMessage(player,`§a[DLavie Heist] SUCCESS §6+$${session.reward.toLocaleString()} §7• §fBalance $${balance.toLocaleString()}`); }
  try {
    system.sendScriptEvent("dlv:heist_complete",JSON.stringify({dimension:session.dimensionId,x:session.blockLocation.x,y:session.blockLocation.y,z:session.blockLocation.z,reward:session.reward,balance,playerId:session.playerId}));
  } catch {}
  cleanupSession(session,"",false);
}

function startSession(player, block, params) {
  if (sessions.has(player.id)) { safeMessage(player,"§e[DLavie Heist] Kamu sedang membobol brankas lain."); return; }
  let opened=false;
  try { opened=block.permutation.getState("dlv:opened") === true; } catch { return; }
  if (opened) { safeMessage(player,"§7[DLavie Heist] Brankas ini sudah kosong."); return; }
  if (!isCrowbarEquipped(player)) { safeMessage(player,"§e[DLavie Heist] Pegang §fCrowbar§e untuk membobol brankas."); return; }
  const durationSeconds=clamp(Number(params.duration_seconds ?? 60),5,600);
  const reward=clamp(Math.floor(Number(params.reward ?? 3000)),1,100000000);
  const maxDistance=clamp(Number(params.max_distance ?? 3.75),1.5,12);
  const blockLocation={x:block.location.x,y:block.location.y,z:block.location.z};
  const dimensionId=block.dimension.id;
  const vaultKey=getVaultKey(dimensionId,blockLocation);
  const owner=reservedVaults.get(vaultKey);
  if (owner && owner !== player.id) { safeMessage(player,"§e[DLavie Heist] Brankas sedang dibobol pemain lain."); return; }
  const center={x:blockLocation.x+0.5,y:blockLocation.y+0.5,z:blockLocation.z+0.5};
  const session={playerId:player.id,dimensionId,blockLocation,center,vaultKey,elapsedTicks:0,durationTicks:Math.floor(durationSeconds*TICKS_PER_SECOND),reward,maxDistanceSq:maxDistance*maxDistance,lastPhase:-1,damaged:false};
  sessions.set(player.id,session);
  reservedVaults.set(vaultKey,player.id);
  try { player.addTag(ACTIVE_TAG); } catch {}
  setInputLocked(player,true);
  cameraShot(player,center,0);
  playPryAnimation(player);
  safeMessage(player,"§6[DLavie Heist] Pembobolan dimulai. Jangan bergerak atau ganti crowbar.");
}

function tickSession(session) {
  const player=getPlayerById(session.playerId);
  if (!player) { sessions.delete(session.playerId); reservedVaults.delete(session.vaultKey); return; }
  if (session.damaged) { failSession(session,"Pembobolan gagal karena kamu terkena damage."); return; }
  if (player.dimension.id !== session.dimensionId) { failSession(session,"Pembobolan dibatalkan karena kamu berpindah dimensi."); return; }
  if (!isCrowbarEquipped(player)) { failSession(session,"Pembobolan dibatalkan karena crowbar tidak lagi di tangan."); return; }
  if (squaredDistance(player.location,session.center) > session.maxDistanceSq) { failSession(session,"Kamu terlalu jauh dari brankas."); return; }
  const block=player.dimension.getBlock(session.blockLocation);
  if (!block || block.typeId !== SAFE_ID) { failSession(session,"Brankas tidak ditemukan."); return; }
  if (block.permutation.getState("dlv:opened") === true) { cleanupSession(session,"Brankas sudah terbuka.",false); return; }
  session.elapsedTicks += 1;
  const progress=clamp(session.elapsedTicks/session.durationTicks,0,1);
  const phase=progress<0.34?0:progress<0.67?1:2;
  if (phase !== session.lastPhase) { session.lastPhase=phase; cameraShot(player,session.center,phase); }
  if (session.elapsedTicks % 24 === 0) playPryAnimation(player);
  if (session.elapsedTicks % 100 === 0) emitHeistNoise(session,player);
  if (session.elapsedTicks % 5 === 0) {
    const remaining=Math.max(0,Math.ceil((session.durationTicks-session.elapsedTicks)/TICKS_PER_SECOND));
    try { player.onScreenDisplay.setActionBar(formatProgress(progress,remaining)); } catch {}
  }
  if (session.elapsedTicks >= session.durationTicks) finishSession(session,player,block);
}
function handleVaultInteract(block, player, params) { if (player && block && block.typeId === SAFE_ID) startSession(player,block,params); }

system.beforeEvents.startup.subscribe((event) => {
  event.blockComponentRegistry.registerCustomComponent("dlv:vault_interaction", {
    onPlayerInteract: (interaction, parameters) => {
      if (!interaction.player) return;
      const params=parameters?.params ?? {};
      system.run(() => handleVaultInteract(interaction.block,interaction.player,params));
    },
  });
});
world.afterEvents.worldLoad.subscribe(() => { try { getMoneyObjective(); } catch {} for (const player of world.getPlayers()) recoverPlayer(player); });
world.afterEvents.playerSpawn.subscribe((event) => {
  system.run(() => {
    recoverPlayer(event.player);
    try { const objective=getMoneyObjective(); if (objective.getScore(event.player) === undefined) objective.setScore(event.player,0); } catch {}
  });
});
world.afterEvents.entityHurt.subscribe((event) => { const session=sessions.get(event.hurtEntity.id); if (session) session.damaged=true; });
world.afterEvents.playerLeave.subscribe((event) => { const session=sessions.get(event.playerId); if (!session) return; sessions.delete(event.playerId); reservedVaults.delete(session.vaultKey); });
system.runInterval(() => { for (const session of [...sessions.values()]) { try { tickSession(session); } catch { failSession(session,"Terjadi error runtime dan pembobolan dibatalkan dengan aman."); } } },1);
system.runInterval(() => {
  for (const player of world.getPlayers()) {
    if (sessions.has(player.id) || player.hasTag(HIDE_HUD_TAG)) continue;
    try { const balance=getMoney(player); player.onScreenDisplay.setActionBar(`§6$${balance.toLocaleString()} §8• §7DLavie`); } catch {}
  }
},40);
