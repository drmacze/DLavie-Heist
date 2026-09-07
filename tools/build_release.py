from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
OUT_DIR = ROOT / "releases" / "v1.2"
OUT = OUT_DIR / "DLavie_Heist_Core_V1.2.mcaddon"

subprocess.check_call([sys.executable, str(ROOT / "tools" / "generate_pbr_assets.py")])

PACKS = [
    (SRC / "behavior_pack", "DLavie_Heist_BP"),
    (SRC / "resource_pack", "DLavie_Heist_RP"),
]

OUT_DIR.mkdir(parents=True, exist_ok=True)
if OUT.exists():
    OUT.unlink()

with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for source, root_name in PACKS:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                arcname = Path(root_name) / path.relative_to(source)
                zf.write(path, arcname.as_posix())

print(OUT)
