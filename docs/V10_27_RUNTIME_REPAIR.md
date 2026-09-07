# DLavie Heist V10.27 — Runtime Repair

Target: Minecraft Bedrock / PE 26.45 integrated AG2 × DLavie build.

## Fixed systems

### Attachments

- Attachment state now has a lore-backed persistence fallback instead of depending only on ItemStack dynamic properties.
- Installed Sight / Muzzle / Underbarrel / Laser data survives inventory moves, backpack serialization, and reloads.
- Selecting a weapon shows the current attachment summary in the action bar and the weapon lore contains the installed loadout.
- Suppressor routing was expanded to remaining supported firing paths: AK12, AK47 CS2, AK60, Glock 18 / Burst, MK16, MP5, AWP/AWPR/AWP Asiimov, and M200.
- Suppressed shots skip normal muzzle flash and loud shot audio and use the silenced sound path.
- Red/green laser runtime continues to use the existing physical attachment prop plus laser-dot particles after the attachment state is restored correctly.

### Backpack

- Fixed the worn backpack render controller referencing the player default geometry instead of `Geometry.dlv_backpack` / `Texture.dlv_backpack`.
- The backpack is rendered as an extra player-bound geometry in third person so it follows the character transform instead of lagging as a teleported prop.
- First/third-person held backpack model scale and position were increased so the item reads clearly as 3D.

### Flashbang

- Removed overlapping nested camera fade commands that could override each other at close range.
- Flashbang detonation is now driven by a dedicated script using one distance tier per player.
- Explicit white RGB fade (`255 255 255`) replaces the black-looking result.
- Added reliable explosion sound + fallback explosion sound, tinnitus, the four existing flashbang particles, camera shake, and longer distance-based recovery.

### Smoking

- Smoking sequence forces `minecraft:first_person` POV at start.
- Fixed the hands render controller: it previously hid all hand geometry whenever an item was selected, including the cigarette.
- Real first-person arms remain rendered while the cigarette attachable and smoking animation play.

## Package validation

Static validation result: **PASS**

- Integrated nested packs: 16
- AG2 repair pack version: `2.7.0`
- Existing AG2 BP/RP UUIDs retained for update-in-place behavior
- Outer ZIP / nested pack CRC: PASS
- Modified JSON parsing: PASS
- Modified JavaScript syntax (`node --check`): PASS
- Full integrated build SHA-256: `424b9e0346ee282f9cdd35661690c44f7a102722d2ddd017675241f511d1a15c`

Runtime testing in Minecraft is still required for visual positioning and device-specific rendering.