# DLavie Survival Stress + Cigarette System V1

Integrated into the local AG2 Delays Ahead / DLavie Heist modpack build. This document records the DLavie-owned integration behavior and compatibility rules; it does not vendor third-party Parkour++ source or assets.

## Stress model

Stress is a persistent 0-100 gameplay stat. It rises from:

- prolonged wakefulness / lack of sleep,
- combat damage and sustained gun use,
- sprinting / high physical exertion,
- low hunger.

Recovery is available through:

- sleeping / sustained bed rest,
- fishing as a quiet activity,
- completing one cigarette use cycle.

## High-stress effects

At elevated stress, the player receives progressively stronger movement slowdown. Higher thresholds add nausea/wave distortion and camera shake. At 100 stress, an untreated delayed collapse timer begins. Dropping stress below the severe range cancels that timer.

If the timer expires, the player enters a short third-person collapse cinematic, movement/camera input is temporarily locked, the screen fades to black, then the player is killed directly. Stress does not apply periodic health damage before the collapse.

## Cigarette item

Identifier: `dlv:cigarette`

- 3D PBR attachable with Color, Normal, and MER maps.
- 15.2 second use duration.
- Three inhale/exhale cycles, spaced approximately five seconds apart.
- First puff includes a lighter/hand-shield movement.
- Custom inhale, exhale, lighter, heartbeat audio and cigarette smoke particle.
- Completing the third puff clears stress to 0 and cancels any pending stress collapse.
- Uses custom player animation rather than the vanilla eating animation.

## Compatibility

- Existing AG2 weapon/ADS runtime is preserved.
- Parkour++ local compatibility build blocks new traversal moves while the `dlv_smoking` tag is active.
- Stress collapse is deferred while `dlv_heist_active` is set so vault cinematics are not interrupted by a second camera controller.
- Bandage/bleeding remains independent from stress.

## Debug helpers

- `/function dlavie/stress_test` sets stress to 100 for testing.
- `/function dlavie/stress_clear` clears stress/awake debt and stress visual effects.

## Release lineage

First integrated full-modpack test target: DLavie Heist V10.24 / AG2 Medical + Stress + ADS V1.8.
