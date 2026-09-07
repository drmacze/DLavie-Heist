# DLavie Heist

Heist gameplay module for **AG2 × DLavie Combat Survival** on Minecraft Bedrock / PE 26.45.

## Latest integrated repair line

**AG2 × DLavie Heist V10.27 — Runtime Repair**

V10.27 repairs the runtime/visual systems reported after V10.26 testing:

- persistent and visible weapon attachments
- functional suppressor audio + muzzle-flash routing
- laser state/beam restoration
- installed attachment info on weapon selection/lore
- character-bound worn backpack geometry + stronger 3D held model
- white flashbang with explosion audio/VFX, tinnitus and longer recovery
- forced first-person smoking POV with visible player hands

See [`docs/V10_27_RUNTIME_REPAIR.md`](docs/V10_27_RUNTIME_REPAIR.md) for the repair and validation details.

> The repository still contains the standalone Heist Core release rather than the complete multi-pack AG2 distribution. The full V10.27 integrated `.mcaddon` is built from the current 16-pack test line and distributed separately.

## Repository Heist module

The standalone Heist module remains available at:

`releases/v10.16/DLavie_Heist_Core_V1.0.mcaddon`

### Heist features

- Custom `dlv:vault_safe` block
- Custom `dlv:crowbar` item
- 60-second vault breach sequence
- 20-segment progress bar with countdown
- Cinematic third-person/free-camera sequence with 3 camera phases
- Repeating crowbar/prying animation
- Breach cancellation when damaged, too far away, or crowbar is removed
- Persistent money objective: `dlv_money`
- Default robbery reward: **$3,000**
- Opened vault state prevents repeat farming
- Metal breach noise integrates with the AG2/DLavie Wanted + hearing system in the full integrated build

## Testing the standalone Heist Core

```mcfunction
/give @s dlv:vault_safe 1
/give @s dlv:crowbar 1
```

Place the safe, hold the crowbar, and interact with the safe.

## Compatibility

- Minecraft Bedrock / PE 26.45 target
- Resource Pack uses PBR capability / modern engine baseline

## V10.27 validation

- Integrated packs: `16`
- AG2 repair pack version: `2.7.0`
- Static ZIP/CRC validation: `PASS`
- Modified JSON parse: `PASS`
- Modified JavaScript syntax: `PASS`
- Full integrated build SHA-256: `424b9e0346ee282f9cdd35661690c44f7a102722d2ddd017675241f511d1a15c`
