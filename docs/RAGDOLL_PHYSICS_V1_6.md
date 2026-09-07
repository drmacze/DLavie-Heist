# DLavie Ragdoll Physics V1.6

V1.6 upgrades the stable-UUID DLavie ragdoll runtime used by the Heist modpack.

## Goals

- Make explosion deaths and already-spawned bodies react with stronger directional tumble rather than rigid translation.
- Allow live player ragdoll on severe projectile impacts, hard wall collisions, and predicted long falls.
- Make projectile hits on corpse limbs local: a hit arm/leg/head snaps first and transfers momentum into the torso.
- Preserve compatibility with AG2 by avoiding any `player.entity.json` override.
- Preserve the existing `realragdoll:spawn` API used by the terrorist combat pack.

## Runtime changes

- Player ragdoll edition enabled and enabled by default.
- New localized impulse solver.
- Projectile impact memory with fallback to `damageSource.damagingProjectile` for cross-pack event-order differences.
- Per-hit projectile zone: head / torso / legs.
- Cumulative projectile stagger; high-energy rounds can knock a surviving player down immediately.
- Existing ragdolled players and NPC/player corpses can be shot and moved at the exact impacted limb.
- Hard-collision watcher detects high-speed upright wall impacts.
- Blast launch uses body-side contact rather than the remote epicentre, reducing unstable torque.
- Blast line-of-sight/occlusion reduces launch force behind cover for players and corpses.
- Secondary blast tumble added.
- Collision response retuned for more body-like friction and lower rubbery restitution.
- Fall takeover remains active and now becomes available because live player ragdoll is enabled.

## DLavie compatibility

The ragdoll pack keeps the same BP/RP UUIDs as V1.5 and only increases the semantic pack version to `1.6.0`.

A compatibility guard checks for `cso:player_corpse_part` before spawning the ragdoll runtime's own dead-player corpse, avoiding duplicate player bodies when the CSO terrorist module owns that proxy.

No AG2 weapon resources or player renderer override are included in this update.

## Static validation

- All JavaScript passes `node --check`.
- All JSON parses.
- BP/RP/MCADDON CRC passes.
- Stable UUIDs preserved.

Exact impact timing and force still require Bedrock device testing because projectile velocity and event ordering can vary across add-ons and engine builds.
