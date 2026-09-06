# DLavie Heist

Immersive robbery gameplay module for **Minecraft Bedrock / PE 26.45**.

## Current build

**DLavie Heist Core v1.2 — Realistic Vault Update**

### Visual overhaul

- Rebuilt `dlv:vault_safe` as a detailed multi-part 3D safe instead of a single cube.
- Separate closed, open-with-cash, and open-empty geometries.
- Visible door thickness, frame, hinges, dial, handle, inner shell, shelves, feet and cash bundles.
- Four PBR safe material stages: pristine, scratched, forced and fully breached.
- Color + normal + MER maps for Vibrant Visuals.
- Resource Pack declares the `pbr` capability.
- Safe rotates to face the player when placed.
- `dlv:crowbar` now has a real held 3D attachable model.
- Crowbar uses a separate inventory icon and 3D PBR material.

### Gameplay overhaul

- 60-second breach with persistent physical damage stages.
- Cancelled attempts preserve the current damage stage instead of visually resetting the safe.
- Resuming a partially damaged safe resumes from its saved stage.
- Relative cinematic camera uses the vault's facing direction instead of fixed world coordinates.
- Camera candidates check nearby air space to reduce clipping into walls.
- Player alignment is attempted before the cinematic when the front position is clear.
- Progressive noise radius for Wanted / hearing integrations.
- Crowbar durability is consumed when the door is successfully forced.
- Opening the door no longer instantly pays money.
- Cash is physically visible inside the open safe.
- Interact with the open safe to collect the reward.
- `dlv:looted` is committed before payout to prevent duplicated rewards.
- Open/looted state persists in the block permutation.
- Per-player sessions and per-vault reservations remain protected.
- Stale movement/camera locks are still recovered after reload/spawn.

### HUD overhaul

The HUD remains **non-invasive** so DLavie Heist does not replace `hud_screen.json` and break minimap/combat UI packs.

During a breach it displays:

- current breach stage
- exact percentage
- 22-segment progress bar
- MM:SS timer
- dynamic LOW / MED / HIGH noise indicator

Start, resume, abort, vault-open, crowbar-break and success states use compact titles/subtitles instead of chat spam.

Idle wallet HUD can be disabled for another HUD pack with:

```mcfunction
/tag @s add dlv_hide_money_hud
```

## Test

```mcfunction
/give @s dlv:vault_safe 1
/give @s dlv:crowbar 1
```

1. Place the safe.
2. Hold the crowbar and interact.
3. Finish the breach.
4. The door opens with cash visible.
5. Interact again to collect the money.

Default reward: **$3,000**.

## Integration events

- `dlv:heist_started`
- `dlv:heist_stage`
- `dlv:heist_noise`
- `dlv:vault_opened`
- `dlv:heist_complete`

## Source layout

```text
src/
  behavior_pack/
  resource_pack/
    attachables/
    models/blocks/
    models/entity/
    textures/blocks/
    textures/items/
tools/
```

## Build and validation

```bash
python -m pip install -r requirements.txt
python tools/generate_pbr_assets.py
python tools/validate_release.py
python tools/build_release.py
```

`build_release.py` and `validate_release.py` also regenerate the deterministic PBR PNG assets automatically.

Output:

```text
releases/v1.2/DLavie_Heist_Core_V1.2.mcaddon
```

## Compatibility

- Minecraft Bedrock / PE 26.45 target
- minimum engine baseline `1.26.40`
- `@minecraft/server` `2.9.0`
- Custom Components V2
- Vibrant Visuals PBR texture sets
