# DLavie Heist Core v1.1 — Debug & Upgrade Report

## Problems addressed

1. **Source was not versioned**
   - v1.0 only stored the compiled `.mcaddon`.
   - v1.1 adds editable Behavior Pack and Resource Pack source under `src/`.

2. **Custom component modernization**
   - The vault uses Custom Components V2 (`dlv:vault_interaction` directly in block components).
   - Registration uses `system.beforeEvents.startup`.

3. **Fail-safe player recovery**
   - Active players receive the persistent `dlv_heist_active` tag.
   - On reload/spawn, stale movement/camera locks are cleared automatically.

4. **Concurrent robbery protection**
   - A vault is reserved while one player is breaching it.
   - Another player cannot start the same vault simultaneously.

5. **Anti-farming / idempotent completion**
   - The vault is switched to `dlv:opened = true` before payout.
   - Opened vaults cannot be robbed again.

6. **Cancellation hardening**
   - Cancels on damage, dimension change, missing vault, excessive distance, or unequipped crowbar.
   - Cleanup always tries to restore movement, camera and HUD state.

7. **Integration events**
   - `dlv:heist_noise` is emitted during the breach.
   - `dlv:heist_complete` is emitted after a successful payout.
   - Other Wanted/AI packs can subscribe through `system.afterEvents.scriptEventReceive`.

8. **HUD compatibility**
   - Money persists in `dlv_money`.
   - Players can add tag `dlv_hide_money_hud` to suppress the standalone action-bar money display if another HUD pack renders the balance.

## Runtime verification still required

Static checks can validate JSON, JavaScript syntax and packaging, but camera framing, animation blending,
touch controls and visual placement must be checked in Minecraft Bedrock/PE 26.45 on a real device.
