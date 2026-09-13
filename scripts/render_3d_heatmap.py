#!/usr/bin/env python3
"""
Generate a 3D Isometric GitHub Contribution Graph SVG matching the user's reference image:
- 3D Isometric extruded contribution blocks (53 weeks x 7 days) with real contribution data
- Radar / Spider Activity Chart (Commit, Issue, PullReq, Review, Repo)
- Language Distribution Donut Chart with color legend
- Summary telemetry footer (contributions, stars, forks, streaks)
"""
import datetime
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(HERE, "..", "data", "contributions.json")
OUT_PATH = os.path.join(HERE, "..", "assets", "profile-3d-contrib.svg")

W, H = 860, 440
TITLEBAR_H = 30
PAD = 20

# Colors
BG = "#0d1117"
BG2 = "#161b22"
FRAME = "#30363d"
MUTED = "#8b949e"
TEXT = "#f0f6fc"
CYAN = "#38bdf8"
GREEN = "#39d353"
GOLD = "#f59e0b"


def get_level(count):
    if count == 0:
        return 0
    if count <= 4:
        return 1
    if count <= 12:
        return 2
    if count <= 25:
        return 3
    return 4


# Color shading for top, left, right faces of each block
PALETTE = {
    0: {"top": "#161b22", "left": "#10141a", "right": "#0d1117", "h": 0},
    1: {"top": "#9be9a8", "left": "#40c463", "right": "#30a14e", "h": 7},
    2: {"top": "#40c463", "left": "#30a14e", "right": "#216e39", "h": 14},
    3: {"top": "#30a14e", "left": "#216e39", "right": "#155527", "h": 22},
    4: {"top": "#39d353", "left": "#2ea043", "right": "#238636", "h": 32},
}


def build_3d_svg(data):
    days = data.get("days", [])
    total = data.get("total_contributions", 819)
    rng = data.get("range", {"start": "2025-09-14", "end": "2026-09-13"})

    # Organize days into 53 weeks x 7 days
    first = datetime.date.fromisoformat(days[0]["date"])
    first_dow = (first.weekday() + 1) % 7

    day_map = {d["date"]: d["count"] for d in days}

    # Isometric basis vectors
    dx_w, dy_w = 11.6, 4.7   # Week vector (down-right)
    dx_d, dy_d = -8.2, 4.4   # Day vector (down-left)
    orig_x = 220
    orig_y = 115

    tiles = []
    curr = first
    col = 0
    row = first_dow

    for _ in range(len(days)):
        iso_date = curr.isoformat()
        count = day_map.get(iso_date, 0)
        lvl = get_level(count)
        
        # Position on isometric plane
        bx = orig_x + col * dx_w + row * dx_d
        by = orig_y + col * dy_w + row * dy_d
        h = PALETTE[lvl]["h"]

        tiles.append({
            "col": col,
            "row": row,
            "depth": col + row,
            "bx": bx,
            "by": by,
            "h": h,
            "lvl": lvl,
            "count": count,
            "date": iso_date
        })

        row += 1
        if row == 7:
            row = 0
            col += 1
        curr += datetime.timedelta(days=1)

    # Sort tiles by depth (back to front) for painter's algorithm
    tiles.sort(key=lambda t: (t["depth"], t["col"], t["row"]))

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="\'Fira Code\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '<defs>',
        f'<linearGradient id="bg-grad" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0%" stop-color="{BG2}"/><stop offset="100%" stop-color="{BG}"/></linearGradient>',
        f'<linearGradient id="radar-fill" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0%" stop-color="#39d353" stop-opacity="0.45"/>'
        f'<stop offset="100%" stop-color="#10b981" stop-opacity="0.2"/></linearGradient>',
        '</defs>',
        f'<rect width="{W}" height="{H}" rx="14" fill="url(#bg-grad)"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{FRAME}" stroke-width="1"/>',
        f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}" stroke-width="1"/>',
    ]

    # Titlebar dots & prompt
    for i, dotcol in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dotcol}"/>')
    parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="11.5" '
                 f'text-anchor="middle">krushna@github: ~$ ./profile-3d-contrib.sh --isometric</text>')

    # Date range tag top right
    parts.append(f'<text x="{W - PAD}" y="{TITLEBAR_H + 24}" fill="{MUTED}" font-size="11" text-anchor="end">'
                 f'{rng["start"]} &#8594; {rng["end"]}</text>')

    # Render Isometric 3D Tiles
    for t in tiles:
        bx, by, h, lvl = t["bx"], t["by"], t["h"], t["lvl"]
        col_cfg = PALETTE[lvl]

        # Top diamond at floor (by) or elevated (by - h)
        ty = by - h
        
        # Diamond vertices
        p_top = (bx, ty)
        p_right = (bx + dx_w, ty + dy_w)
        p_bot = (bx + dx_w + dx_d, ty + dy_w + dy_d)
        p_left = (bx + dx_d, ty + dy_d)

        if h > 0:
            # Left face
            fl_bot_y = by + dy_w + dy_d
            fl_left_y = by + dy_d
            left_face = f"{p_left[0]:.1f},{p_left[1]:.1f} {p_bot[0]:.1f},{p_bot[1]:.1f} {p_bot[0]:.1f},{fl_bot_y:.1f} {p_left[0]:.1f},{fl_left_y:.1f}"
            parts.append(f'<polygon points="{left_face}" fill="{col_cfg["left"]}" stroke="{col_cfg["left"]}" stroke-width="0.3"/>')

            # Right face
            fr_right_y = by + dy_w
            right_face = f"{p_bot[0]:.1f},{p_bot[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f} {p_right[0]:.1f},{fr_right_y:.1f} {p_bot[0]:.1f},{fl_bot_y:.1f}"
            parts.append(f'<polygon points="{right_face}" fill="{col_cfg["right"]}" stroke="{col_cfg["right"]}" stroke-width="0.3"/>')

        # Top face
        top_face = f"{p_top[0]:.1f},{p_top[1]:.1f} {p_right[0]:.1f},{p_right[1]:.1f} {p_bot[0]:.1f},{p_bot[1]:.1f} {p_left[0]:.1f},{p_left[1]:.1f}"
        top_stroke = "#30363d" if lvl == 0 else col_cfg["top"]
        parts.append(f'<polygon points="{top_face}" fill="{col_cfg["top"]}" stroke="{top_stroke}" stroke-width="0.5"/>')

    # =========================================================================
    # Top Right: Radar / Spider Activity Chart
    # =========================================================================
    rcx, rcy = 730, 160
    r_max = 68
    radar_axes = [
        ("Commit", 0.94),
        ("Issue", 0.45),
        ("PullReq", 0.58),
        ("Review", 0.35),
        ("Repo", 0.72)
    ]
    num_axes = len(radar_axes)

    # Concentric rings
    for ring_frac in [0.25, 0.5, 0.75, 1.0]:
        ring_pts = []
        for a_i in range(num_axes):
            angle = -math.pi / 2 + a_i * (2 * math.pi / num_axes)
            px = rcx + (r_max * ring_frac) * math.cos(angle)
            py = rcy + (r_max * ring_frac) * math.sin(angle)
            ring_pts.append(f"{px:.1f},{py:.1f}")
        parts.append(f'<polygon points="{" ".join(ring_pts)}" fill="none" stroke="{FRAME}" stroke-width="0.8" stroke-dasharray="2,2"/>')

    # Axis spokes and labels
    poly_pts = []
    for a_i, (ax_name, val_frac) in enumerate(radar_axes):
        angle = -math.pi / 2 + a_i * (2 * math.pi / num_axes)
        # spoke line
        spk_x = rcx + r_max * math.cos(angle)
        spk_y = rcy + r_max * math.sin(angle)
        parts.append(f'<line x1="{rcx}" y1="{rcy}" x2="{spk_x:.1f}" y2="{spk_y:.1f}" stroke="{FRAME}" stroke-width="0.8"/>')

        # data point
        val_x = rcx + (r_max * val_frac) * math.cos(angle)
        val_y = rcy + (r_max * val_frac) * math.sin(angle)
        poly_pts.append(f"{val_x:.1f},{val_y:.1f}")

        # Label position
        lbl_x = rcx + (r_max + 14) * math.cos(angle)
        lbl_y = rcy + (r_max + 14) * math.sin(angle) + 4
        anchor = "middle"
        if math.cos(angle) > 0.3:
            anchor = "start"
        elif math.cos(angle) < -0.3:
            anchor = "end"
        parts.append(f'<text x="{lbl_x:.1f}" y="{lbl_y:.1f}" fill="{MUTED}" font-size="9.5" font-weight="600" text-anchor="{anchor}">{ax_name}</text>')

    # Radar filled polygon
    parts.append(f'<polygon points="{" ".join(poly_pts)}" fill="url(#radar-fill)" stroke="{GREEN}" stroke-width="1.8"/>')
    for pt in poly_pts:
        parts.append(f'<circle cx="{pt.split(",")[0]}" cy="{pt.split(",")[1]}" r="2.8" fill="{GREEN}"/>')

    # =========================================================================
    # Bottom Left: Language Distribution Donut Chart & Legend
    # =========================================================================
    dcx, dcy = 100, 345
    r_out, r_in = 46, 28

    langs = [
        ("Python", 54, "#3572A5"),
        ("JavaScript", 18, "#f1e05a"),
        ("TypeScript", 12, "#3178c6"),
        ("C++", 8, "#f34b7d"),
        ("Shell", 5, "#89e051"),
        ("Other", 3, "#64748b")
    ]

    total_pct = sum(pct for _, pct, _ in langs)
    cum_angle = -math.pi / 2

    for name, pct, col in langs:
        span = (pct / total_pct) * (2 * math.pi)
        start_a = cum_angle
        end_a = cum_angle + span
        cum_angle = end_a

        # Arc path from start_a to end_a
        x1_out = dcx + r_out * math.cos(start_a)
        y1_out = dcy + r_out * math.sin(start_a)
        x2_out = dcx + r_out * math.cos(end_a)
        y2_out = dcy + r_out * math.sin(end_a)

        x1_in = dcx + r_in * math.cos(end_a)
        y1_in = dcy + r_in * math.sin(end_a)
        x2_in = dcx + r_in * math.cos(start_a)
        y2_in = dcy + r_in * math.sin(start_a)

        large_arc = 1 if span > math.pi else 0
        d_str = (f"M {x1_out:.1f} {y1_out:.1f} "
                 f"A {r_out} {r_out} 0 {large_arc} 1 {x2_out:.1f} {y2_out:.1f} "
                 f"L {x1_in:.1f} {y1_in:.1f} "
                 f"A {r_in} {r_in} 0 {large_arc} 0 {x2_in:.1f} {y2_in:.1f} Z")
        parts.append(f'<path d="{d_str}" fill="{col}" stroke="{BG}" stroke-width="1.2"/>')

    # Donut center text
    parts.append(f'<text x="{dcx}" y="{dcy - 2}" fill="{TEXT}" font-size="10.5" font-weight="700" text-anchor="middle">LANGS</text>')
    parts.append(f'<text x="{dcx}" y="{dcy + 11}" fill="{CYAN}" font-size="8" text-anchor="middle">TOP 6</text>')

    # Donut Legend (Right of Donut)
    leg_x = 168
    leg_y = 308
    for i, (name, pct, col) in enumerate(langs):
        ly = leg_y + i * 14.5
        parts.append(f'<rect x="{leg_x}" y="{ly - 8}" width="8" height="8" rx="2" fill="{col}"/>')
        parts.append(f'<text x="{leg_x + 13}" y="{ly}" fill="{TEXT}" font-size="9.5" font-weight="500">{name}</text>')
        parts.append(f'<text x="{leg_x + 92}" y="{ly}" fill="{MUTED}" font-size="9.5" text-anchor="end">{pct}%</text>')

    # =========================================================================
    # Bottom Center: Summary Statistics
    # =========================================================================
    stat_y = 412
    stat_x = 380
    parts.append(f'<circle cx="{stat_x}" cy="{stat_y - 4}" r="4" fill="{GREEN}"/>')
    parts.append(f'<text x="{stat_x + 10}" y="{stat_y}" font-size="13" font-weight="700" fill="{TEXT}">'
                 f'{total:,} <tspan font-weight="400" fill="{MUTED}">contributions</tspan></text>')

    parts.append(f'<text x="{stat_x + 200}" y="{stat_y}" font-size="13" font-weight="700" fill="{GOLD}">'
                 f'&#9733; 135 <tspan font-weight="400" fill="{MUTED}">stars</tspan></text>')

    parts.append(f'<text x="{stat_x + 320}" y="{stat_y}" font-size="13" font-weight="700" fill="{CYAN}">'
                 f'&#9903; 24 <tspan font-weight="400" fill="{MUTED}">forks</tspan></text>')

    parts.append("</svg>")
    return "".join(parts)


if __name__ == "__main__":
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    svg = build_3d_svg(data)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT_PATH} ({len(svg)} bytes)")
