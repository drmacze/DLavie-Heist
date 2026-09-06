#!/usr/bin/env python3
from pathlib import Path
import json, zipfile

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "src" / "behavior_pack"
RP = ROOT / "src" / "resource_pack"
OUT = ROOT / "releases" / "v1.1" / "DLavie_Heist_Core_V1.1.mcaddon"

def validate_json_tree(path):
    for file in path.rglob("*.json"):
        with file.open("r", encoding="utf-8") as f:
            json.load(f)

def add_tree(zf, base, prefix):
    for file in sorted(base.rglob("*")):
        if file.is_file():
            zf.write(file, f"{prefix}/{file.relative_to(base).as_posix()}")

def main():
    validate_json_tree(BP)
    validate_json_tree(RP)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        OUT.unlink()
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        add_tree(zf, BP, "DLavie_Heist_BP")
        add_tree(zf, RP, "DLavie_Heist_RP")
    print(OUT)

if __name__ == "__main__":
    main()
