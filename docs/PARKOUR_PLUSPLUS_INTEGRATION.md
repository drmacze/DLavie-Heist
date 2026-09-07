# Parkour++ integration for DLavie Heist

Parkour++ is integrated into the local DLavie Heist modpack as the replacement for the older S7D parkour runtime.

## Source / rights

The Parkour++ add-on was supplied by the user. It is owned by Se7enDays Studio (S7D) and its bundled license prohibits redistribution/modification/re-upload without permission. Therefore the public DLavie-Heist repository does **not** vendor the Parkour++ source or binary. This document only records the local compatibility strategy used when building from the user-supplied pack.

## Local compatibility changes

- Keep Parkour++ traversal systems: Slide, Roll, Dropkick, Vault, Wallrun, Crawl, Dodge, Aqua Dash and Ledge Grab.
- Keep Parkour++ Smart Watch, settings, particles, animations and PBR resources.
- Remove the older S7D parkour BP/RP from the full suite so two movement runtimes cannot trigger at once.
- Disable Parkour++'s permanent `Player.applyKnockback` monkey patch. Direct per-move Parkour++ knockback/velocity calls remain intact.
- Replace the world-wide `fallDamage` gamerule toggling used by Roll/Wallrun with player-local `fallDistance` protection.
- Do not start a new traversal move while the player is in DLavie Heist lock/spectator states, swimming, gliding, riding or holding the Trauma Bandage.
- For Actual Guns 2, do not start a new traversal move while crouched/ADS, reloading, drawing, inspecting or during recent firearm use.
- If a parkour move has already started, allow it to finish naturally rather than abruptly cancelling the animation/state.
- Parkour++ does not ship a `hud_screen.json` override or a client/behavior `minecraft:player` entity override in the integrated build, avoiding the main AG2 HUD/player-render conflicts.

## Full-suite baseline

The local V10.23 build combines:

- AG2 Delays Ahead × DLavie Medical + ADS V1.7
- Parkour++ by S7D with the compatibility changes above
- DLavie Heist Core v1.4
- DLavie Ragdoll Runtime v1.5
- DLavie Tactical Flashlight v1.1
- DLavie Ballistic Block Physics v1.1
- Aplok Equipment Lite v1.2
- CSO Terrorist Combat Overhaul v8

Runtime behavior still requires Bedrock/PE device testing, especially transitions between ADS and Slide/Dodge, gun firing during parkour, Roll/Wallrun fall protection, and Heist cinematic/spectator gating.
