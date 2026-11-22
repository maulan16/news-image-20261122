"""news-image-20261122 entry: copy the pre-rendered broadsheet to /output/entry.png.

The image is drawn by build.py (Pillow) from stories.py and committed as entry.png.
This program only needs the standard library.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    # sanity: a whole PNG, within the 1 MiB gate
    assert data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) <= 1 << 20
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
