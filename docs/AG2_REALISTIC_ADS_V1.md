# Actual Guns 2 × DLavie TRUE ADS

This integration is developed for **Actual Guns 2: Delays Ahead** used by the DLavie Heist modpack. It is not part of the cancelled CS2-ONLINE experiment.

## Current test build: V1.5 Refined TRUE ADS

V1.5 builds on **V1.4 TRUE ADS / V1.3.2 Render Recovery**, keeping the proven render-safe first-person stack while adding device-tuned per-family calibration and safer motion variety.

### Core behavior

- Crouch/sneak enters ADS.
- Vanilla `+` crosshair stays hidden whenever an AG2 firearm is equipped.
- Aim is intended to use the weapon's own iron sight / optic geometry.
- Native AG2 sniper zoom remains authoritative.
- Existing V1.1 recoil is preserved.
- The creative-mode infinite-ammo warning is limited to 5 seconds.

### V1.5 device-tuned corrections

Based on on-device screenshots:

- **M4A1 / M4A1-S / M16A1** receive a stronger sight-line correction: the complete first-person assembly is raised and centered further while ADS so the rear/front sight can be used as the actual aiming reference.
- **SVI Infinity Single family** keeps its good native ADS motion, but the `infinity` weapon bone is scaled to roughly **1.22–1.25×** because the gun model appeared too small compared with the arms. This correction scales the weapon only, not the hands/player rig.
- Garand, MP5 and AK-family calibration is refined conservatively rather than globally shifting every firearm.
- Pistol families that already looked correct remain intentionally conservative.

### Safe motion architecture

The important safety rule remains: no new global player/root/arm animation controller.

- Every firearm controller keeps its original AG2 ADS state and first-person ADS animation.
- V1.5 adds a small state-scoped per-family ADS micro-sway.
- V1.5 adds state-scoped idle/sprint movement on the `body` bone only, with different profiles for rifle, heavy rifle, SMG, pistol and sniper families.
- Motion phase differs per controller so all weapons do not bob in exact sync.
- Reload, draw, fire and native inspect states remain authoritative and are not replaced by the new motion layer.
- The only non-body V1.5 correction is the SVI `infinity` weapon-bone scale fix.

### Coverage

- 53 integrated AG2 firearm item IDs remain in the all-in-one Delays Ahead build.
- 33 firearm controller families preserve native ADS.
- 33/33 receive V1.5 per-family ADS calibration/micro-sway.
- 33/33 receive safe state-scoped idle/sprint motion.
- Native scope/optic behavior remains authoritative for AWP/AWPR/M200.

### ADS FOV

- rifle: 64
- pistol: 69
- SMG: 66
- sniper: native AG2 zoom

## Runtime testing priority

Exact iron-sight alignment remains visual. Prioritize M4A1/M4A1-S/M16A1 and SVI Infinity Single variants in V1.5, then inspect Garand, MP5, AK-family and remaining rifles. Any remaining misalignment should be tuned per weapon family only; do not modify the global first-person rig.
