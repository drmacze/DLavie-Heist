# DLavie Heist Core v1.4
Minecraft Bedrock / PE 26.45 heist gameplay core.

## v1.4
- Squad death loop: dead players become Spectator; when the whole active squad is dead, everyone returns to their captured spawn point.
- Every player death creates a 3D PBR `dlv:ag2_grave_loot` cache. Loot is generated only from the 79 Actual Guns item IDs present in the target AG2 build (guns, magazines/ammo, grenades, melee).
- Vault front orientation corrected. Interaction from the rear panel is rejected.
- Vault alignment stays on the physical door side and has a fallback for carpet/slab-style floor probes.
- Four mandatory interactive breach checks with increasing setbacks/noise.
- Four close cinematic phases, all on the front side of the safe; no intentional far/behind-wall shot.
- Expanded character motion: lock inspection, crowbar wedge, left/right pry, shoulder lever, handle turn, door pull, cash collection and cash stow.
- Cash collection is animated and reserved to one player before payout.
- Gravestone uses deterministic 256px Color + Normal + MER PBR resources for Vibrant Visuals. No AI image generation is used.

### Test
```mcfunction
/give @s dlv:vault_safe 1
/give @s dlv:crowbar 1
```
Use alongside the same Actual Guns build used by the DLavie suite. The grave system gracefully skips unavailable item IDs if AG2 is not installed.

The exact v1.4 code/JSON source snapshot is stored at `source_snapshots/DLavie_Heist_Core_V1.4_CODE_ONLY.tar.gz`; generated PBR PNG assets are shipped in the release build.
