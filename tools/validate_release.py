#!/usr/bin/env python3
from pathlib import Path
import json, zipfile, subprocess, sys

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "src" / "behavior_pack"
RP = ROOT / "src" / "resource_pack"
RELEASE = ROOT / "releases" / "v1.1" / "DLavie_Heist_Core_V1.1.mcaddon"

errors = []

def check_json_tree(path):
    for file in path.rglob("*.json"):
        try:
            json.loads(file.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"JSON {file}: {exc}")

check_json_tree(BP)
check_json_tree(RP)

bp_manifest = json.loads((BP / "manifest.json").read_text(encoding="utf-8"))
rp_manifest = json.loads((RP / "manifest.json").read_text(encoding="utf-8"))

rp_uuid = rp_manifest["header"]["uuid"]
deps = bp_manifest.get("dependencies", [])
if not any(d.get("uuid") == rp_uuid for d in deps):
    errors.append("BP manifest does not depend on RP UUID")
if not any(d.get("module_name") == "@minecraft/server" and d.get("version") == "2.9.0" for d in deps):
    errors.append("Missing @minecraft/server 2.9.0 dependency")

block = json.loads((BP / "blocks" / "vault_safe.json").read_text(encoding="utf-8"))
components = block["minecraft:block"]["components"]
if components.get("minecraft:destructible_by_mining") is not False:
    errors.append("Vault must be indestructible by mining")
if components.get("minecraft:destructible_by_explosion") is not False:
    errors.append("Vault must be indestructible by explosion")
params = components.get("dlv:vault_interaction", {})
if params.get("duration_seconds") != 60:
    errors.append("Vault duration must be 60 seconds")
if params.get("reward") != 3000:
    errors.append("Vault reward must be 3000")

script = (BP / "scripts" / "main.js").read_text(encoding="utf-8")
required = ["system.beforeEvents.startup", "registerCustomComponent", "InputPermissionCategory.Movement", "InputPermissionCategory.Camera", "dlv:heist_noise", "dlv:heist_complete", "dlv_heist_active"]
for token in required:
    if token not in script:
        errors.append(f"Missing script token: {token}")

node = subprocess.run(["node", "--check", str(BP / "scripts" / "main.js")], capture_output=True, text=True)
if node.returncode:
    errors.append("JavaScript syntax: " + node.stderr.strip())

if not RELEASE.exists():
    errors.append("Release .mcaddon missing")
else:
    try:
        with zipfile.ZipFile(RELEASE) as zf:
            bad = zf.testzip()
            if bad:
                errors.append(f"ZIP CRC failed: {bad}")
            names = set(zf.namelist())
            required_paths = {"DLavie_Heist_BP/manifest.json", "DLavie_Heist_BP/scripts/main.js", "DLavie_Heist_BP/blocks/vault_safe.json", "DLavie_Heist_RP/manifest.json", "DLavie_Heist_RP/textures/terrain_texture.json", "DLavie_Heist_RP/animations/heist_player.animation.json"}
            missing = sorted(required_paths - names)
            if missing:
                errors.append("Release missing: " + ", ".join(missing))
    except Exception as exc:
        errors.append(f"Release ZIP invalid: {exc}")

if errors:
    print("VALIDATION: FAIL")
    for error in errors:
        print("- " + error)
    sys.exit(1)

print("VALIDATION: PASS")
print("- JSON strict parse")
print("- JavaScript syntax")
print("- manifest dependency closure")
print("- 60 second / $3000 config")
print("- Custom Components V2 registration")
print("- input lock + recovery hooks")
print("- integration script events")
print("- ZIP CRC and required release files")
