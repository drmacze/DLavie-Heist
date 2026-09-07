# Actual Guns 2 × DLavie TRUE ADS

This integration is developed for **Actual Guns 2: Delays Ahead** used by the DLavie Heist modpack. It is not part of the cancelled CS2-ONLINE experiment.

## Current test build: V1.4 TRUE ADS

V1.4 is rebuilt from the **V1.3.2 Render Recovery / proven V1.1 first-person baseline**, because that baseline is confirmed on-device to keep hands and weapons visible.

### Core behavior

- Crouch/sneak enters ADS.
- Vanilla `+` crosshair stays hidden whenever an AG2 firearm is equipped.
- Aim is intended to use the weapon's own iron sight / optic geometry.
- Native AG2 sniper zoom remains authoritative.
- Existing V1.1 recoil and restrained weapon sway are preserved.
- The creative-mode infinite-ammo warning is limited to 5 seconds.

### V1.4 iron-sight calibration architecture

The important safety rule is that V1.4 does **not** replace the global player/root/arm animation stack.

- Every firearm controller keeps its original AG2 ADS state and original first-person ADS animation.
- Weak/off-center ADS families receive a second, state-scoped calibration animation.
- Calibration animations touch the `body` bone only, moving the complete first-person assembly together.
- They never directly override `root`, `rightArm`, `leftArm`, or individual gun bones, avoiding the hand/weapon disappearance regression seen in experimental V1.2/V1.3 motion builds.
- Strong native ADS/scope families are preserved with little or no correction.

### Coverage

- 53 integrated AG2 firearm item IDs remain in the all-in-one Delays Ahead build.
- 33 firearm controller families retain a native ADS state.
- 28 controller families receive state-scoped calibration overlays.
- Native scope/optic behavior is preserved for AWP/AWPR/M200 and other already-strong scope families.

### Refined generic ADS FOV

- rifle: 64
- pistol: 69
- SMG: 66
- sniper: native AG2 zoom

The lower FOV values make aligned iron sights easier to read without bringing back the vanilla crosshair.

## Runtime testing priority

Exact sight alignment is ultimately visual and should be verified on-device. First validate M4A1/M4A1S/M16A1, AK47/AKM, MP5, Desert Eagle variants, then the remaining firearm families. If a specific sight is slightly high/low/left/right, tune that family only rather than modifying the global first-person rig.
