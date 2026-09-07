# DLavie Medical V1.7

Integrated directly into the **Actual Guns 2: Delays Ahead × DLavie** all-in-one build.

## Trauma Bandage
- Item ID: `dlv:trauma_bandage`
- 3.2 second use time.
- Uses `minecraft:use_animation: none`; the player does not use the vanilla eating motion.
- Dedicated first-person and third-person arm-wrapping animations move the right hand around the left forearm in repeated wrapping/tightening passes.
- 3D attachable model with a bandage roll, core and loose cloth strip.
- Deterministic 256px PBR resources: color, normal and MER textures. No AI image generation is used.
- Crafting recipe produces 4 bandages from white wool + string.

## Medical effect
On a completed bandage use:
- active bleeding is stopped;
- wound protection reduces re-bleed chance for 20 seconds;
- health is restored gradually: 1 HP every 2 seconds, up to 6 HP total;
- no instant heal burst is applied.

## Bleeding system
Player damage can create bleeding depending on cause and damage amount.
- Projectile damage has the highest normal bleed chance.
- Entity attacks have a medium chance.
- Explosions have a high chance.
- Significant falls can cause bleeding.
- Fire/lava/drowning/starvation/magic are excluded from wound bleeding.

Bleeding has three severities. Higher severity causes blood-loss ticks more often. Existing AG2 blood particles and heartbeat audio are reused for feedback. Bandaging removes the bleeding state and resets the severity.

## Safety
This feature is integrated without replacing the proven first-person gun render stack or the V1.6 ADS fallback system. The bandage animation only runs while `dlv:trauma_bandage` is actively being used.
