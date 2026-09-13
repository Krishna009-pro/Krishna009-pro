"""
Build the anime coder card SVG:
Features a single, stunning anime AI developer illustration in a dark cyberpunk command center,
framed in a sleek cyber-cyan rounded card with ZERO text, matching avi-ascii.svg in height.
"""
import base64
import io
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
SRC_IMG = os.path.join(HERE, "..", "assets", "anime_coder.jpg")

TARGET_W = 980
TARGET_H = 770

def generate_card():
    if not os.path.exists(SRC_IMG):
        raise FileNotFoundError(f"Source image not found: {SRC_IMG}")

    im = Image.open(SRC_IMG)
    orig_w, orig_h = im.size
    target_aspect = TARGET_W / TARGET_H
    orig_aspect = orig_w / orig_h

    if orig_aspect > target_aspect:
        new_w = int(orig_h * target_aspect)
        offset = (orig_w - new_w) // 2
        cropped = im.crop((offset, 0, offset + new_w, orig_h))
    else:
        new_h = int(orig_w / target_aspect)
        offset = (orig_h - new_h) // 2
        cropped = im.crop((0, offset, orig_w, offset + new_h))

    resized = cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    resized.save(buf, format="JPEG", quality=86, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{TARGET_W}" height="{TARGET_H}" viewBox="0 0 {TARGET_W} {TARGET_H}">
  <defs>
    <linearGradient id="card-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#161b22"/>
      <stop offset="100%" stop-color="#0d1117"/>
    </linearGradient>
    <linearGradient id="border-glow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#1e293b" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.4"/>
    </linearGradient>
    <clipPath id="card-clip">
      <rect x="2" y="2" width="{TARGET_W - 4}" height="{TARGET_H - 4}" rx="14" />
    </clipPath>
  </defs>

  <!-- Background Base -->
  <rect width="{TARGET_W}" height="{TARGET_H}" rx="16" fill="url(#card-bg)"/>

  <!-- Anime Coder Illustration (Single Image, No Text) -->
  <g clip-path="url(#card-clip)">
    <image href="data:image/jpeg;base64,{b64}" x="0" y="0" width="{TARGET_W}" height="{TARGET_H}" preserveAspectRatio="xMidYMid slice"/>
  </g>

  <!-- Sleek Cyber Glass Frame -->
  <rect x="0.5" y="0.5" width="{TARGET_W - 1}" height="{TARGET_H - 1}" rx="16" fill="none" stroke="url(#border-glow)" stroke-width="1.5"/>
  <rect x="1.5" y="1.5" width="{TARGET_W - 3}" height="{TARGET_H - 3}" rx="15" fill="none" stroke="#30363d" stroke-width="1" opacity="0.4"/>
</svg>
"""

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"Generated {OUT} ({os.path.getsize(OUT)} bytes)")

if __name__ == "__main__":
    generate_card()
