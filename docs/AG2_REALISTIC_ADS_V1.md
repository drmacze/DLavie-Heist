# Actual Guns 2 × DLavie TRUE ADS

This integration is developed for **Actual Guns 2: Delays Ahead** used by the DLavie Heist modpack. It is not part of the cancelled CS2-ONLINE experiment.

## Current test build: V1.6 ADS Fallback

V1.6 builds on **V1.5 Refined TRUE ADS**, preserving the render-safe first-person stack and the per-family alignment work while simplifying weak ADS behavior around two proven on-device motion references: **MK16** and **AKM**.

### Core behavior

- Crouch/sneak enters ADS.
- Vanilla `+` crosshair stays hidden whenever an AG2 firearm is equipped.
- Aim is intended to use the weapon's own iron sight / optic geometry.
- Native AG2 sniper zoom remains authoritative.
- Existing V1.1 recoil and V1.5 safe idle/sprint motion are preserved.
- The creative-mode infinite-ammo warning is limited to 5 seconds.

### V1.6 fallback policy

The user confirmed that MK16 and AKM have good ADS movement on-device. Weak/static rifle ADS therefore no longer gets a newly invented transition style.

- **MK16-style fallback:** M4A1, M4A1-S, M16A1, MP5 and MR6.
- **AKM-style fallback:** AK47, AK47R, AK60 and M1 Garand.
- Good pistol ADS is intentionally left unchanged.
- Strong native scope/optic families such as AWP/AWPR/M200 stay fully native.
- AK12 and F2000 keep their stronger native animated ADS.

The fallback does **not** copy another weapon's raw arm/gun animation file directly because AG2 families use different weapon-bone names and raw reuse can break first-person rendering. Instead, V1.6 transfers the proven MK16/AKM bring-up timing and trajectory as a **transient BODY-only ADS entry layer** on top of each weapon's own native AG2 first-person animation and its V1.5 final sight alignment.

This keeps each weapon's hands, gun bones, reload/draw/fire animation and skin geometry authoritative while producing the same style of shoulder-to-sight movement.

### Safety architecture

- No global player/root/arm controller is added.
- New V1.6 fallback animations touch the `body` bone only.
- Original AG2 `root`, `leftArm`, `rightArm`, magazine and weapon-specific bones remain owned by the native weapon animation.
- V1.5 final per-family iron-sight alignment remains underneath the transient V1.6 entry animation.
- The V1.6 layer settles to zero at the end, so it cannot continuously push the weapon away from its calibrated ADS point.

### Coverage

- 53 integrated AG2 firearm IDs remain in the all-in-one Delays Ahead build.
- 9 weak/static rifle-family controllers receive V1.6 fallback entry motion.
- 5 receive MK16-style timing.
- 4 receive AKM-style timing.
- Pistol families and native optic/sniper families are not replaced.

## Runtime testing priority

Prioritize M4A1/M4A1-S/M16A1 first, then MP5/MR6, AK47/AK47R/AK60 and M1 Garand. Exact final iron-sight alignment remains device-visual; fallback motion should be tuned only per family and must not modify the global first-person rig.
