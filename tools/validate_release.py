from pathlib import Path
import json
import subprocess
import sys
import zipfile
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
subprocess.check_call([sys.executable, str(ROOT / "tools" / "generate_pbr_assets.py")])
BP = ROOT / "src" / "behavior_pack"
RP = ROOT / "src" / "resource_pack"
OUT = ROOT / "releases" / "v1.2" / "DLavie_Heist_Core_V1.2.mcaddon"

errors = []

def fail(message):
    errors.append(message)

for root in (BP, RP):
    for path in root.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"JSON: {path.relative_to(ROOT)}: {exc}")

try:
    rpm = json.loads((RP / "manifest.json").read_text())
    if "pbr" not in rpm.get("capabilities", []): fail("RP manifest is missing pbr capability")
    if rpm["header"]["version"] != [1, 2, 0]: fail("RP version is not 1.2.0")
except Exception as exc: fail(f"RP manifest: {exc}")

try:
    bpm = json.loads((BP / "manifest.json").read_text())
    if bpm["header"]["version"] != [1, 2, 0]: fail("BP version is not 1.2.0")
    if not any(d.get("module_name") == "@minecraft/server" and d.get("version") == "2.9.0" for d in bpm.get("dependencies", [])): fail("@minecraft/server 2.9.0 dependency is missing")
except Exception as exc: fail(f"BP manifest: {exc}")

for ts in list((RP / "textures" / "blocks").glob("*.texture_set.json")) + list((RP / "textures" / "items").glob("*.texture_set.json")):
    try:
        data = json.loads(ts.read_text())["minecraft:texture_set"]
        for key in ("color", "normal", "metalness_emissive_roughness"):
            ref = data.get(key)
            if not isinstance(ref, str): fail(f"{ts.name}: missing string {key}"); continue
            png = ts.parent / f"{ref}.png"
            if not png.exists(): fail(f"{ts.name}: missing {png.name}")
    except Exception as exc: fail(f"Texture set {ts.name}: {exc}")

expected_pngs=[RP/"textures/blocks/vault_safe.png",RP/"textures/blocks/vault_safe_normal.png",RP/"textures/blocks/vault_safe_mer.png",RP/"textures/blocks/vault_safe_stage3.png",RP/"textures/items/crowbar_3d.png",RP/"textures/items/crowbar_3d_normal.png",RP/"textures/items/crowbar_3d_mer.png",RP/"textures/items/crowbar_icon.png"]
for path in expected_pngs:
    if not path.exists(): fail(f"Missing texture {path.relative_to(ROOT)}"); continue
    try:
        with Image.open(path) as im: im.verify()
    except Exception as exc: fail(f"PNG {path.name}: {exc}")

try:
    block=json.loads((BP/"blocks/vault_safe.json").read_text())["minecraft:block"]
    states=block["description"]["states"]
    for state in ("dlv:opened","dlv:looted","dlv:breach_stage"):
        if state not in states: fail(f"Missing block state {state}")
    text=(BP/"blocks/vault_safe.json").read_text()
    for geo in ("geometry.dlv.vault_safe.closed","geometry.dlv.vault_safe.open_cash","geometry.dlv.vault_safe.open_empty"):
        if geo not in text: fail(f"Missing geometry reference {geo}")
except Exception as exc: fail(f"Block validation: {exc}")

try:
    attach=json.loads((RP/"attachables/crowbar.attachable.json").read_text()); desc=attach["minecraft:attachable"]["description"]
    if desc.get("identifier")!="dlv:crowbar": fail("Crowbar attachable identifier mismatch")
    if desc.get("geometry",{}).get("default")!="geometry.dlv.crowbar": fail("Crowbar geometry reference mismatch")
except Exception as exc: fail(f"Crowbar attachable: {exc}")

script=BP/"scripts/main.js"; text=script.read_text(encoding="utf-8")
for token in ('registerCustomComponent("dlv:vault_interaction"','"dlv:looted"','"dlv:breach_stage"','ItemComponentTypes.Durability','"dlv:vault_opened"','"dlv:heist_complete"','formatProgressHud','cameraCandidateIsClear'):
    if token not in text: fail(f"Script missing token: {token}")
try:
    result=subprocess.run(["node","--check",str(script)],capture_output=True,text=True)
    if result.returncode!=0: fail("JavaScript syntax: "+(result.stderr or result.stdout))
except FileNotFoundError: print("WARN: node not installed; JS syntax check skipped")

if OUT.exists():
    try:
        with zipfile.ZipFile(OUT) as zf:
            bad=zf.testzip()
            if bad: fail(f"ZIP CRC failed: {bad}")
    except Exception as exc: fail(f"MCADDON: {exc}")

if errors:
    print("VALIDATION: FAIL")
    for error in errors: print(" -",error)
    sys.exit(1)
print("VALIDATION: PASS")
