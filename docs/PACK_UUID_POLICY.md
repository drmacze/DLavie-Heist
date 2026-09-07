# DLavie Heist Stable UUID Policy

From this point forward, every maintained DLavie Heist pack must keep its established header/module UUIDs across updates. New releases increment only the semantic pack version unless a deliberate hard reset is required.

## AG2 Delays Ahead × DLavie

Stable IDs established by the Definitive line:

- Behavior Pack header: `dd5dac7a-678f-4a27-a2fd-0decdc708327`
- Behavior data module: `9a0399e1-96d3-4b06-a65f-cf0220556616`
- Behavior script module: `ec128ecf-402a-4361-a786-c8f39fa44e2c`
- Resource Pack header: `fc3c92f2-b40c-40a3-ad0f-fe0e4cfd6415`
- Resource module: `af22dda7-20ea-4015-89e0-afb71f30fc55`

V2.1 increments the pack/module version to `2.1.0` while preserving every UUID above so Minecraft imports it as an update rather than another duplicate pack.

## Other DLavie Heist packs

Parkour, NPC/combat, Heist Core, ragdoll, gore, equipment and future maintained packs follow the same rule: once a pack UUID has been adopted in a shipped DLavie build, later revisions preserve that UUID and bump only the version. Dependency versions must be updated together with the target pack version.

Do not regenerate UUIDs for ordinary feature updates, bug fixes, animation revisions, texture upgrades or compatibility changes.
