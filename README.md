# DLavie Heist

Heist gameplay module for **AG2 × DLavie Combat Survival** on Minecraft Bedrock / PE 26.45.

## Latest integrated build

**AG2 × DLavie Combat Survival V10.16 — Heist Core**

The repository currently includes the standalone Heist module extracted from the V10.16 integrated build:

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
- Metal breach noise integrates with the AG2/DLavie Wanted + hearing system in the full V10.16 build

## Testing

```mcfunction
/give @s dlv:vault_safe 1
/give @s dlv:crowbar 1
```

Place the safe, hold the crowbar, and interact with the safe.

## Compatibility

- Minecraft Bedrock / PE 26.45 target
- `@minecraft/server` 2.9.0
- Resource Pack uses PBR capability / modern engine baseline

## V10.16 integrated build

Full integrated build metadata:

- File: `AG2_DLavie_Combat_Survival_V10_16_HEIST_CORE_ALL_IN_ONE.mcaddon`
- Size: `12,345,216 bytes`
- SHA-256: `8565341d58015169fa4e72a6614f2c34bae135755cec88274c3b622333d07b06`
- Internal packs: `15`

See `docs/V10_16_HEIST_CORE_VALIDATION.txt` for validation details.
