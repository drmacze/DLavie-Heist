# DLavie Tactical Backpack — AG2 Definitive V2.4

This document describes the DLavie tactical backpack integration for the stable-UUID Actual Guns 2 pack used by DLavie Heist.

## Core design

- Stable AG2 UUIDs are preserved; V2.4 only bumps the pack version to `2.4.0`.
- Backpack item: `dlv:tactical_backpack`.
- Capacity: 24 persistent storage slots and 32.0 kg maximum carried weight.
- Storage uses player dynamic properties so backpack contents survive normal script reloads and do not depend on a hidden container entity remaining loaded.
- Item serialization preserves identifier, amount, custom name, lore, durability, enchantments, and ItemStack dynamic properties. This is specifically important for AG2 weapons because attachment metadata is stored as ItemStack dynamic properties.
- The backpack itself cannot be packed inside its own storage.

## UI

The backpack opens from one tap of Use while holding the backpack. The UI includes:

- current kg / maximum kg;
- slots used / 24;
- visual load bar and load-state text;
- Contents / Withdraw;
- Pack Item from player inventory;
- Quick Pack for ammo, food, medical, attachment and material supplies;
- Weight Analysis grouped by category;
- Sort Load by weight;
- Wear / hide visual backpack model.

## Weight gameplay

Weight is calculated using category-aware item masses. Weapons, magazines, grenades, armor, blocks, food, tools and survival supplies use different unit weights. A deposit is capped by remaining weight and available slots.

At 95%+ capacity the player receives a mild Slowness I effect while the backpack is present, plus the `dlv_backpack_heavy` tag. The effect is refreshed briefly rather than globally clearing Slowness, so the existing DLavie stress system can still apply stronger stress-related movement penalties independently.

## Visual / physics model

The visual backpack is a custom `dlv:backpack_prop` entity that follows the player while the model is enabled. It has a detailed model with:

- main pack shell;
- front compartment;
- top carry handle;
- left/right side pouches;
- shoulder straps;
- loose hanging strap ends;
- chest buckle;
- zipper pulls;
- MOLLE webbing;
- hydration tube;
- bottom roll;
- DLavie patch.

The model uses a memory-safe 512px PBR material set: Color, Normal and MER.

Secondary motion is driven by synchronized entity properties rather than replacing the global player animation rig. Separate states cover idle, walking, sprinting, airborne motion and heavy load. Loose straps, zipper pulls, side pouches, hydration tube and bottom roll sway independently so the pack does not look rigid while moving.

## Compatibility safety

The backpack feature does not replace or edit AG2 weapon animation controllers. Attachment runtime, Stress/Cigarette, Bandage/Bleeding and V2.3 grenade files remain unchanged apart from the V2.4 manifest/main runtime import.
