# Actual Guns 2 × DLavie Realistic ADS V1

This integration is developed for the Actual Guns 2 build used by the DLavie Heist full modpack.

## Behavior

- Crouch/sneak enters ADS for firearm classes.
- Vanilla `+` crosshair is hidden whenever an AG2 firearm is equipped.
- Aim is performed with the weapon's iron sight / optic model.
- Native AG2 sniper zoom is preserved rather than replaced by the generic FOV controller.
- Procedural first-person weapon sway gives hip-fire more movement and ADS a smaller breathing sway.
- Firing controllers receive deterministic rotational camera kick with class-specific strength and per-controller variance.

## V1 coverage

- 208 AG2 firearm items tagged for the ADS runtime.
- 335 firing states patched across 156 firing-controller files.
- Classes: rifles, pistols, SMGs, snipers, shotguns, heavy and equipment firearms.

Generic ADS FOV targets:

- pistol: 76
- SMG: 73
- rifle: 70
- shotgun: 72
- heavy: 68
- equipment: 66
- sniper: native AG2 zoom

## Important runtime note

The current `gyro-style` behavior means procedural inertial viewmodel sway plus camera recoil. Bedrock add-ons do not expose the iPhone's physical gyroscope sensor to Molang weapon animations.

Per-model X/Y/Z ADS calibration is the next tuning stage: the universal controller works across the gun set, but individual iron sights can require alignment offsets because AG2 weapon geometries differ.

## Build provenance

V1 was generated from the same Actual Guns 2/full DLavie V10.22 input used by the Heist modpack. It is not a CS2-ONLINE feature. Future revisions belong to this repository/project.
