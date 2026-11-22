"""Render the 22 November 2026 broadsheet to entry.png (1024x1024, deterministic).

Run: python3 build.py   (needs Pillow and the DejaVu / Noto fonts; main.py does not)
"""
from PIL import Image, ImageDraw, ImageFont

from stories import DATE_LINE, HEROES, REGIONS, MARKETS, MARKETS_NOTE, SOURCES_NOTE

N_STORIES = len(HEROES) + sum(len(r[2]) for r in REGIONS)

W = H = 1024
PAPER = (246, 241, 230)
INK = (22, 20, 18)
GREY = (95, 90, 82)
RULE = (40, 36, 32)

FD = "/usr/share/fonts/truetype/"
SERIF_B = FD + "noto/NotoSerif-Bold.ttf"
SERIF = FD + "noto/NotoSerif-Regular.ttf"
SANS_B = FD + "noto/NotoSans-Bold.ttf"
SANS = FD + "noto/NotoSans-Regular.ttf"

_cache = {}


def font(path, size):
    key = (path, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(path, size)
    return _cache[key]


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(draw, y, text, fnt, fill=INK):
    tw = draw.textlength(text, font=fnt)
    draw.text(((W - tw) / 2, y), text, font=fnt, fill=fill)


def draw_building(d, x, y, s):
    """Apartment block with a collapsed corner, smoke and a drone above."""
    # block
    d.rectangle([x, y + s * 0.30, x + s * 0.62, y + s], fill=(120, 112, 100), outline=INK, width=2)
    # broken corner (polygon cut out with paper colour, then rubble)
    d.polygon([(x + s * 0.40, y + s * 0.30), (x + s * 0.62, y + s * 0.30),
               (x + s * 0.62, y + s * 0.70), (x + s * 0.50, y + s * 0.52)], fill=PAPER)
    for i in range(5):
        rx = x + s * (0.50 + 0.06 * (i % 3))
        ry = y + s * (0.84 + 0.04 * (i % 2))
        d.rectangle([rx, ry, rx + s * 0.07, ry + s * 0.12], fill=(90, 84, 76))
    # windows: 5 floors
    for fl in range(5):
        for c in range(3):
            wx = x + s * (0.06 + 0.12 * c)
            wy = y + s * (0.36 + 0.125 * fl)
            if c == 2 and fl < 2:
                continue
            d.rectangle([wx, wy, wx + s * 0.07, wy + s * 0.07], fill=(235, 200, 90))
    # smoke
    for i, (ox, oy, r) in enumerate([(0.56, 0.22, 0.09), (0.66, 0.13, 0.11), (0.78, 0.05, 0.08)]):
        cx, cy, rr = x + s * ox, y + s * oy, s * r
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=(150, 146, 140))
    # drone: delta wing
    dx, dy = x + s * 0.92, y + s * 0.10
    d.polygon([(dx - s * 0.12, dy), (dx + s * 0.06, dy - s * 0.06), (dx + s * 0.02, dy + s * 0.07)], fill=INK)
    d.line([(dx - s * 0.12, dy), (dx - s * 0.25, dy + s * 0.12)], fill=(180, 30, 30), width=2)


def draw_thermo(d, x, y, s):
    """Earth with a thermometer past a 1.5 mark."""
    r = s * 0.36
    cx, cy = x + s * 0.40, y + s * 0.55
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 130, 180), outline=INK, width=2)
    d.polygon([(cx - r * 0.5, cy - r * 0.6), (cx + r * 0.1, cy - r * 0.7), (cx + r * 0.2, cy - r * 0.1),
               (cx - r * 0.3, cy + r * 0.2)], fill=(90, 150, 80))
    d.polygon([(cx + r * 0.3, cy + r * 0.2), (cx + r * 0.7, cy + r * 0.3), (cx + r * 0.4, cy + r * 0.8)],
              fill=(90, 150, 80))
    # thermometer
    tx = x + s * 0.86
    d.rounded_rectangle([tx - s * 0.06, y + s * 0.02, tx + s * 0.06, y + s * 0.84], radius=s * 0.06,
                        fill=(250, 250, 250), outline=INK, width=2)
    d.ellipse([tx - s * 0.11, y + s * 0.78, tx + s * 0.11, y + s * 1.0], fill=(200, 30, 30), outline=INK, width=2)
    d.rectangle([tx - s * 0.03, y + s * 0.18, tx + s * 0.03, y + s * 0.82], fill=(200, 30, 30))
    mark = y + s * 0.32
    d.line([(tx - s * 0.13, mark), (tx + s * 0.13, mark)], fill=INK, width=2)
    d.text((tx - s * 0.16 - 34, mark - 10), "1.5\u00b0", font=font(SANS_B, 15), fill=INK)


ART = {"building": draw_building, "thermo": draw_thermo}


def masthead(d):
    d.rectangle([0, 0, W, 8], fill=INK)
    centered(d, 10, "THE WORLD IN ONE DAY", font(SERIF_B, 50))
    d.line([(24, 76), (W - 24, 76)], fill=RULE, width=2)
    d.line([(24, 80), (W - 24, 80)], fill=RULE, width=1)
    f = font(SANS_B, 19)
    d.text((26, 84), DATE_LINE, font=f, fill=(170, 20, 20))
    right = f"{N_STORIES} STORIES  \u00b7  {len(REGIONS)} DESKS  \u00b7  MARKETS"
    d.text((W - 26 - d.textlength(right, font=f), 84), right, font=f, fill=INK)
    d.line([(24, 110), (W - 24, 110)], fill=RULE, width=2)


def heroes(d, top, bottom):
    colw = (W - 48 - 20) / 2
    for i, h in enumerate(HEROES):
        x0 = 24 + i * (colw + 20)
        art = 118
        ART[h["art"]](d, x0, top + 8, art)
        tx = x0 + art + 26
        tw = colw - art - 26
        d.text((tx, top + 4), h["kicker"], font=font(SANS_B, 14), fill=(170, 20, 20))
        y = top + 22
        for ln in wrap(d, h["head"], font(SERIF_B, 23), tw):
            d.text((tx, y), ln, font=font(SERIF_B, 23), fill=INK)
            y += 27
        y += 2
        for ln in wrap(d, h["deck"], font(SERIF, 13), tw):
            d.text((tx, y), ln, font=font(SERIF, 13), fill=GREY)
            y += 16
        assert y <= bottom, ("hero overflow", h["head"], y)
        if i == 0:
            d.line([(x0 + colw + 10, top), (x0 + colw + 10, bottom - 6)], fill=RULE, width=1)
    d.line([(24, bottom), (W - 24, bottom)], fill=RULE, width=2)


def region_box(d, x0, y0, w, h, name, colour, items):
    d.rectangle([x0, y0, x0 + w, y0 + 24], fill=colour)
    d.text((x0 + 8, y0 + 2), name, font=font(SANS_B, 16), fill=(255, 255, 255))
    f = font(SERIF, 13)
    y = y0 + 30
    for it in items:
        lines = wrap(d, it, f, w - 18)
        d.rectangle([x0 + 2, y + 6, x0 + 8, y + 12], fill=colour)
        for ln in lines:
            d.text((x0 + 13, y), ln, font=f, fill=INK)
            y += 15
        y += 5
    assert y <= y0 + h, ("region overflow", name, y, y0 + h)
    return y


def markets(d, top):
    d.rectangle([0, top, W, H], fill=INK)
    d.text((24, top + 6), "MARKETS", font=font(SANS_B, 16), fill=(240, 200, 60))
    d.text((24, top + 28), MARKETS_NOTE, font=font(SANS, 11), fill=(200, 200, 200))
    x = 250
    step = (W - x - 20) / len(MARKETS)
    for name, val, chg in MARKETS:
        d.text((x, top + 6), name, font=font(SANS_B, 13), fill=(220, 220, 220))
        col = (110, 210, 120) if chg.startswith("+") else (240, 100, 90)
        d.text((x, top + 24), (val + " " + chg).strip(), font=font(SANS_B, 14), fill=col if chg else (230, 230, 230))
        x += step


def render(path="entry.png"):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    masthead(d)
    heroes(d, 116, 274)
    # row 1: four regions, row 2: three
    top1, top2, mtop = 282, 668, 972
    cols4 = (W - 48 - 3 * 12) / 4
    for i, (name, colour, items) in enumerate(REGIONS[:4]):
        region_box(d, 24 + i * (cols4 + 12), top1, cols4, top2 - top1, name, colour, items)
    d.line([(24, top2 - 6), (W - 24, top2 - 6)], fill=RULE, width=1)
    cols3 = (W - 48 - 2 * 12) / 3
    for i, (name, colour, items) in enumerate(REGIONS[4:]):
        end = region_box(d, 24 + i * (cols3 + 12), top2, cols3, mtop - top2, name, colour, items)
        if i == 0:  # sources note fills the space under the Africa desk
            y = end + 8
            d.line([(24, y - 4), (24 + cols3, y - 4)], fill=RULE, width=1)
            for ln in wrap(d, SOURCES_NOTE, font(SANS, 11), cols3 - 4):
                d.text((26, y), ln, font=font(SANS, 11), fill=GREY)
                y += 14
            assert y <= mtop
    markets(d, mtop)
    img.save(path, format="PNG", optimize=True)


if __name__ == "__main__":
    render()
