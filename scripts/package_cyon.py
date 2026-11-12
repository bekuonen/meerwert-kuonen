"""Package the built static website, excluding the former external CMS."""
from pathlib import Path
import sys
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parents[1] / "public"
if len(sys.argv) != 2 or not (root / "index.html").is_file():
    raise SystemExit("Run hugo --minify, then package_cyon.py OUTPUT.zip")
with ZipFile(sys.argv[1], "w", ZIP_DEFLATED) as archive:
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if path.is_file() and relative.parts[0] != "admin":
            archive.write(path, relative)
