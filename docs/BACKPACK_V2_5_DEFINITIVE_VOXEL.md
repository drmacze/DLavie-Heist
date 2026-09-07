# DLavie Definitive Backpack V2.5

V2.5 upgrades the integrated AG2/DLavie backpack while preserving the stable AG2 BP/RP UUIDs.

## Storage and load

- Mk.I Standard: 24 slots / 32 kg.
- Mk.II Reinforced: 30 slots / 40 kg.
- Mk.III Expedition: 36 slots / 48 kg.
- V2.4 slot data migrates in place; the original first 24 dynamic-property slot keys are unchanged.
- Near full capacity the player receives a mild movement penalty.
- Weapon metadata, durability, enchantments, lore and AG2 attachment dynamic properties are serialized with the stored ItemStack.

## UI

The backpack dashboard includes Contents/Search, Pack Item, Quick Access pinning, Quick Pack, Load Intelligence, Organize Load, Frame Upgrade and Backpack Systems controls.

## Safety fixes

- Deposit now re-checks the selected player inventory stack after UI interaction before removing it, reducing stale-slot duplication/loss risk.
- Invalid/corrupted backpack slot JSON is cleared rather than repeatedly breaking reads.
- Sorting preserves Quick Access priority.
- The fixed `32 kg` item display string was removed because capacity can now be upgraded.

## Definitive Voxel model

- Geometry increased from 16 bones / 37 cubes to 29 bones / 214 cubes.
- 152 micro-cubes form MOLLE loops, stitching, zipper teeth, bungee lattice, hardware, pouch webbing, compression straps and other small 3D details.
- Articulated strap chains, segmented hydration tube, carabiner, D-rings and compression straps add secondary motion.
- Voxel detail can be switched to an Optimized mode from the backpack UI.
- This uses standard Bedrock entity cube geometry and does not require Experimental toggles.

## Secondary-motion physics

Backpack motion now reacts to idle, walk, sprint, crouch, airborne, turning and landing states. Load ratio drives pack/pouch deformation and heavy/overload sag. Physics quality can be set to High, Balanced or Eco, affecting prop-follow update cadence without touching the AG2 weapon/ADS rig.

## Compatibility

V2.5 intentionally leaves non-backpack AG2 systems unchanged. Static comparison against V2.4 found 1140 BP files and 1477 RP files unchanged outside the intended backpack/manifest changes.
