"""Reproduce Fig. 7/8 image crops from the preserved, one-page poster.

Requires Poppler's pdftoppm and Pillow. Crop coordinates are fractions of the
full poster, measured from the top left. No curves or pixels are redrawn.
"""

from pathlib import Path
import subprocess
import tempfile

from PIL import Image


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "references/fan-3d-printed-surface-trap-qccd-poster.pdf"
OUTPUT = HERE / "figures"
CROPS = {
    "poster-transport-voltages.png": (0.435, 0.695, 0.668, 0.823),
    "poster-transport-endpoints.png": (0.696, 0.696, 0.961, 0.821),
}


def main():
    OUTPUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="transport-poster-") as temp:
        prefix = Path(temp) / "poster"
        subprocess.run([
            "pdftoppm", "-f", "1", "-singlefile", "-scale-to", "6000",
            "-png", str(SOURCE), str(prefix),
        ], check=True)
        with Image.open(prefix.with_suffix(".png")) as poster:
            width, height = poster.size
            for filename, rectangle in CROPS.items():
                box = tuple(round(value * (width if i % 2 == 0 else height))
                            for i, value in enumerate(rectangle))
                poster.crop(box).save(OUTPUT / filename)


if __name__ == "__main__":
    main()
