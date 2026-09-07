# AG2 × DLavie Attachment System V2.1

V2.1 adds a DLavie-owned modular attachment runtime to the AG2 Delays Ahead Definitive build. The behavior is independently implemented for AG2 compatibility; the user's supplied Aplok pack was used as a local reference/source for the requested attachment/table feature and its table visual assets are not committed to this public repository.

## Attachment slots

- Sight
- Muzzle
- Underbarrel
- Laser

## Attachments

- OKP-7 Reflex Sight
- Holographic Sight
- ACOG 4×
- LPVO Tactical Scope
- High-Power Scope
- Predator V4 Smart Sight
- Tactical Suppressor
- Vertical Foregrip
- Red Laser Module
- Green Laser Module

Attachments are stored on the individual AG2 ItemStack via dynamic properties, so two copies of the same gun may carry different loadouts.

## Workbenches

- Attachment Workbench: install/remove compatible attachments while holding an AG2 firearm.
- Weapon Workbench: view the installed loadout, detach all, and save/apply Preset A.
- Ammo Workbench: fabricate existing AG2 AR, pistol, SMG and sniper magazine items from vanilla field materials.

## Runtime enhancements

- Compatible options are filtered by rifle/pistol/SMG/sniper class and special cases such as dual pistols and M1 Garand.
- Optics modify ADS FOV without replacing AG2's existing animation/controller stack.
- Red and green laser modules provide a raycast laser impact dot.
- Existing AG2 weapon controllers, animation files, gun items and projectile resources remain byte-identical to the V2.0.1 baseline apart from the main script import and resource atlas registration.
- V2.1 keeps the established AG2 BP/RP/module UUIDs and increments versions to 2.1.0.

Exact physical rail-mounted attachment meshes on every AG2 viewmodel are intentionally kept separate from the first runtime integration because AG2 weapon families use different skeletons/geometry. Visual rail-mesh work should be implemented per family without replacing the proven first-person controller stack.
