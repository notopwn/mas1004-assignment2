"""Apply the recorded visual review of 160 sampled training photos.

Run through uv from the repository root. No photos are deleted.
Only clear visible text is excluded; uncertain cases and numbers-only
images are retained. The remainder of the full dataset was not reviewed.
"""
import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    with (ROOT / "scripts/text_photo_review.csv").open(newline="") as source:
        reviewed = list(csv.DictReader(source))
    paths = [row["path"] for row in reviewed if row["decision"] == "exclude_visible_text"]
    assert len(paths) == len(set(paths)), "Duplicate reviewed path"
    assert all((ROOT / "data/starter/train" / path).is_file() for path in paths)
    selection = ROOT / "track_a/selection.csv"
    if selection.exists():
        with selection.open(newline="") as source:
            selected = {row["path"] for row in csv.DictReader(source)}
        paths = [path for path in paths if path in selected]
    if paths:
        subprocess.run([sys.executable, str(ROOT / "src/curate.py"), "drop",
                        *paths, "--reason", "contains letters"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(ROOT / "src/curate.py"), "count"],
                   cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
