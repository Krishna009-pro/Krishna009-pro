"""
Build a neofetch-style info card SVG with embedded avatar / tech graphic,
system specs, and architecture focus -- styled in sleek Cyber Cyan / GitHub Dark theme.
"""
import base64
import html
import io
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
POSTER_PATH = os.path.join(HERE, "..", "assets", "krishna_superhero_poster.jpg")
STATIC = bool(os.environ.get("STATIC"))

W, H = 480, 376
PAD = 16
TITLEBAR_H = 30
KEY_X = PAD
VAL_X = PAD + 68
LINE_H = 20.5

BG = "#0d1117"
BG2 = "#161b22"
FRAME = "#30363d"
MUTED = "#8b949e"
INK = "#f0f6fc"
KEY = "#38bdf8"       # cyber cyan keys
SECTION = "#818cf8"   # electric indigo section headers
GREEN = "#39d353"     # emerald accent
ACCENT = "#38bdf8"    # electric cyan

HOST = "krushna"      # shown as krushna@github in the header

ROWS = [
    ("host",),
    ("kv", "OS", "Ubuntu 24.04 LTS"),
    ("kv", "Host", "Workstation // AI-Node"),
    ("kv", "Kernel", "6.8.0-custom-ai"),
    ("kv", "Uptime", "B.Tech (2024–2028)"),
    ("kv", "Shell", "zsh 5.9 (tmux)"),
    ("kv", "Editor", "VS Code & Neovim"),
    ("kv", "Compute", "NVIDIA CUDA · TensorRT"),
    ("gap",),
    ("sec", "Architecture & R&D"),
    ("kv", "AI Core", "Multi-Agent Routing"),
    ("kv", "Backends", "AsyncIO Event Loops"),
    ("kv", "Vision", "Defect Detection & CV"),
    ("kv", "Standard", "Strict Type Contracts"),
]


def esc(s):
    return html.escape(s)


def get_avatar_b64():
    """Crops and optimizes krishna_superhero_poster.jpg to an avatar."""
    if not os.path.exists(POSTER_PATH):
        return None
    try:
        im = Image.open(POSTER_PATH)
        # Crop upper torso with head and Python fire (848x1264)
        crop_box = (70, 110, 780, 1080)
        cropped = im.crop(crop_box)
        cropped.thumbnail((260, 360), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        cropped.save(buf, format="JPEG", quality=82, optimize=True)
        return base64.b64encode(buf.getvalue()).decode("ascii")
    except Exception as e:
        print("Avatar crop error:", e)
        return None


def rise(inner, i):
    """fade + slight upward slide, staggered by row index."""
    if STATIC:
        return f"<g>{inner}</g>"
    delay = 0.12 + i * 0.04
    return (f'<g opacity="0" transform="translate(0,5)">{inner}'
            f'<animate attributeName="opacity" from="0" to="1" begin="{delay:.2f}s" dur="0.4s" fill="freeze"/>'
            f'<animateTransform attributeName="transform" type="translate" from="0 5" to="0 0" '
            f'begin="{delay:.2f}s" dur="0.4s" fill="freeze" calcMode="spline" keySplines="0.2 0.8 0.2 1"/></g>')


avatar_b64 = get_avatar_b64()

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="\'Fira Code\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
    '<defs>',
    f'<linearGradient id="ibg" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0%" stop-color="{BG2}"/><stop offset="100%" stop-color="{BG}"/></linearGradient>',
    f'<linearGradient id="avatar-glow" x1="0" y1="0" x2="1" y2="1">'
    f'<stop offset="0%" stop-color="#38bdf8" stop-opacity="0.6"/>'
    f'<stop offset="100%" stop-color="#818cf8" stop-opacity="0.3"/></linearGradient>',
    '<clipPath id="avatar-clip">'
    '<rect x="323" y="52" width="138" height="210" rx="8" />'
    '</clipPath>',
    '</defs>',
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#ibg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]

for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')
parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
             f'text-anchor="middle">{esc(HOST)}@github: ~$ neofetch</text>')

# Right side: Cyber avatar container with character image
parts.append(f'''
  <!-- Avatar Card Container -->
  <g transform="translate(0, 0)">
    <rect x="321" y="50" width="142" height="298" rx="10" fill="#111827" stroke="{FRAME}" stroke-width="1"/>
    <rect x="321.5" y="50.5" width="141" height="297" rx="10" fill="none" stroke="url(#avatar-glow)" stroke-width="1"/>
''')

if avatar_b64:
    parts.append(f'''
    <!-- Embedded Character Image -->
    <image href="data:image/jpeg;base64,{avatar_b64}" xlink:href="data:image/jpeg;base64,{avatar_b64}" 
           x="323" y="52" width="138" height="210" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)"/>
''')
else:
    # Vector fallback
    parts.append(f'''
    <rect x="323" y="52" width="138" height="210" rx="8" fill="#1f2937"/>
    <circle cx="392" cy="140" r="32" fill="#0284c7" fill-opacity="0.2" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="392" y="145" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle">AI CORE</text>
''')

parts.append(f'''
    <!-- Status & Telemetry Tag -->
    <circle cx="337" cy="278" r="3.5" fill="{GREEN}">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="348" y="281.5" fill="{GREEN}" font-size="9" font-weight="700" letter-spacing="0.5">CORE ACTIVE</text>
    
    <rect x="329" y="295" width="126" height="20" rx="4" fill="#0b0f19" stroke="{FRAME}" stroke-width="1"/>
    <text x="392" y="308.5" fill="#38bdf8" font-size="9" font-weight="700" text-anchor="middle" letter-spacing="0.5">KRISHNA // DEV</text>
    
    <text x="392" y="332" fill="{MUTED}" font-size="8" text-anchor="middle">AGENTIC &#183; PYTHON</text>
  </g>
''')

# Left side: Specs & Architecture Focus
y = TITLEBAR_H + 28
for i, row in enumerate(ROWS):
    kind = row[0]
    if kind == "gap":
        y += LINE_H * 0.4
        continue
    if kind == "host":
        host = esc(HOST)
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" font-size="13" font-weight="700">'
                 f'<tspan fill="{KEY}">{host}</tspan><tspan fill="{MUTED}">@</tspan>'
                 f'<tspan fill="{SECTION}">github</tspan></text>'
                 f'<line x1="{KEY_X + 110}" y1="{y-4:.1f}" x2="310" y2="{y-4:.1f}" '
                 f'stroke="{FRAME}" stroke-opacity="0.8"/>')
    elif kind == "sec":
        title = esc(row[1])
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" fill="{SECTION}" font-size="11.5" font-weight="700">'
                 f'&#8212; {title}</text>'
                 f'<line x1="{KEY_X + 145}" y1="{y-4:.1f}" x2="310" y2="{y-4:.1f}" '
                 f'stroke="{FRAME}" stroke-opacity="0.8"/>')
    elif kind == "kv":
        key, val = esc(row[1]), esc(row[2])
        inner = (f'<text x="{KEY_X}" y="{y:.1f}" fill="{KEY}" font-size="11" font-weight="700">{key}</text>'
                 f'<text x="{VAL_X}" y="{y:.1f}" fill="{INK}" font-size="11">{val}</text>')
    else:
        continue
    parts.append(rise(inner, i))
    y += LINE_H

parts.append("</svg>")
svg = "".join(parts)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print("wrote", OUT, len(svg), "bytes;", W, "x", H, "content_bottom", round(y))
