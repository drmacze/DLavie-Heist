# DLavie Heist

Heist gameplay module for **Minecraft Bedrock / PE 26.45**.

## Current development build

**DLavie Heist Core v1.1**

The repository now contains editable Behavior Pack / Resource Pack source plus reproducible build and validation tools. The packaged v1.1 `.mcaddon` can be generated from source with the build command below.

### Main gameplay

- `dlv:vault_safe` robbery block
- `dlv:crowbar` tool
- 60-second breach
- 20-segment progress HUD
- 3-phase cinematic free camera
- custom prying animation
- cancel on damage / distance / dimension change / crowbar removal
- persistent `dlv_money` scoreboard
- default reward `$3,000`
- opened-state anti-farming
- simultaneous-vault reservation
- recovery from stale movement/camera locks after script reload
- script events for Wanted / hearing integration

## Source layout

```text
src/
  behavior_pack/
    blocks/vault_safe.json
    items/crowbar.json
    scripts/main.js
  resource_pack/
    animations/
    models/
    textures/
tools/build_release.py
tools/validate_release.py
```

## Build

```bash
python tools/build_release.py
python tools/validate_release.py
```

Output:

```text
releases/v1.1/DLavie_Heist_Core_V1.1.mcaddon
```

## Test commands

```mcfunction
/give @s dlv:vault_safe 1
/give @s dlv:crowbar 1
```

Place the safe, hold the crowbar and interact with the safe.

To hide the standalone money action bar when another DLavie HUD renders money:

```mcfunction
/tag @s add dlv_hide_money_hud
```

## Compatibility

- Minecraft Bedrock / PE 26.45 target
- minimum engine baseline `1.26.40`
- `@minecraft/server` `2.9.0`
- Custom Components V2

See `docs/V1_1_DEBUG_REPORT.md` for the debugging notes.
