# DLavie Heist v1.2 — Debug & Upgrade Report

## Problems visible in the v1.1 test screenshots

1. The vault read visually as a textured cube instead of a heavy steel safe.
2. The front face had almost no physical depth.
3. The held crowbar was still dominated by a flat item presentation.
4. Cinematic camera positions were world-axis based, so shots could land behind nearby structures.
5. Breach HUD was functional but visually noisy and lacked clear gameplay stages.
6. Successful breach immediately paid the reward, so the visible money inside the safe had no gameplay role.
7. The safe had only an opened state; there was no separate looted state.
8. Cancelling a breach lost all visual damage feedback.

## v1.2 changes

### 3D / PBR

- Multi-part safe shell with a real hollow interior.
- Hinged door geometry has separate closed/open poses.
- Open-with-cash and open-empty geometries.
- PBR Color + Normal + MER texture sets for four safe damage stages.
- Dedicated polished hardware, dark interior and non-metal cash regions.
- 3D crowbar attachable and geometry.
- Dedicated crowbar normal/MER maps and inventory icon.
- RP `pbr` capability enabled.

### Gameplay

- Added `dlv:looted` and `dlv:breach_stage` block states.
- Damage stages 0–3 persist after cancellation.
- Saved stage maps to resumed breach progress.
- Door opens first; money is collected in a separate interaction.
- Loot state commits before scoreboard payout.
- Crowbar wear is applied only after a successful breach.
- Camera is calculated relative to safe facing and checks candidate air space.
- Progressive heist noise events now include radius, level and progress.

### HUD

- Replaced large start chat feedback with title/subtitle states.
- Two-line action bar shows stage, percentage, progress, timer and noise.
- Success HUD separates `VAULT OPEN` from final `HEIST SUCCESS`.
- Wallet HUD remains optional via `dlv_hide_money_hud`.
- No `hud_screen.json` override is shipped, preserving compatibility with existing tactical/minimap HUD packs.

## Runtime items that still require device testing

Static validation cannot prove:
- exact first-person crowbar pose on every device/FOV,
- final camera framing in every possible room layout,
- PBR appearance under every Vibrant Visuals preset,
- animation blending with every third-party player animation pack.

Those are the focus of the next on-device test.
