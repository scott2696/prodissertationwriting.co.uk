#!/usr/bin/env python3
"""Draw the author avatars as monograms.

These are deliberately NOT photographs. Inventing a stock face for a named
reviewer is a false trust signal, and a face is the one EEAT element you cannot
honestly synthesise. Replace these files with real photographs of the real
people at the same paths and sizes (64px, and @2x at 128px) before launch.
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "images", "authors")
os.makedirs(OUT, exist_ok=True)

PEOPLE = [("daniel-mercer", "DM", (10, 38, 34)), ("priya-raman", "PR", (21, 69, 61))]
CITRINE = (226, 163, 60)


def font(sz):
    for path in ("/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
                 "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
                 "/Library/Fonts/Arial Bold.ttf"):
        if os.path.exists(path):
            return ImageFont.truetype(path, sz)
    return ImageFont.load_default()


for slug, initials, ground in PEOPLE:
    S = 512
    im = Image.new("RGB", (S, S), ground)
    d = ImageDraw.Draw(im)
    d.ellipse((int(S * .06),) * 2 + (int(S * .94),) * 2, outline=CITRINE, width=int(S * .035))
    f = font(int(S * .40))
    box = d.textbbox((0, 0), initials, font=f)
    d.text(((S - (box[2] - box[0])) / 2 - box[0], (S - (box[3] - box[1])) / 2 - box[1]),
           initials, font=f, fill=(255, 255, 255))
    im.resize((64, 64), Image.LANCZOS).save(os.path.join(OUT, "%s.jpg" % slug), quality=92)
    im.resize((128, 128), Image.LANCZOS).save(os.path.join(OUT, "%s@2x.jpg" % slug), quality=92)
    print("wrote", slug)
