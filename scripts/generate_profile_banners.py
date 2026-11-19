"""
Generate custom Cyber Cyan, Electric Blue, and Deep Indigo themed engineering SVG assets
for Krushna Patil's GitHub profile:
  1. assets/hero-banner.svg          - Clean cyber-indigo hero banner with architecture diagram
  2. assets/engineering-pillars.svg  - 3-column engineering cards (AI, Backend, Vision)
  3. assets/engineering-workflow.svg - 4-step workflow loop (Clarify, Architect, Benchmark, Ship)
  4. assets/footer-banner.svg        - Clean telemetry architecture footer banner
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
os.makedirs(ASSETS, exist_ok=True)


def generate_hero_banner():
    """Builds the 860x145 minimalist Black Clover / Cyber Cyan hero banner."""
    out_path = os.path.join(ASSETS, "hero-banner.svg")
    W, H = 860, 145
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <!-- Dark Grimoire Obsidian Background -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="45%" stop-color="#0b101e"/>
      <stop offset="85%" stop-color="#140a17"/>
      <stop offset="100%" stop-color="#1a0916"/>
    </linearGradient>

    <!-- Cyber-Cyan to Anti-Magic Crimson Dual Beam -->
    <linearGradient id="accent-beam" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.95"/>
      <stop offset="40%" stop-color="#3b82f6" stop-opacity="0.9"/>
      <stop offset="75%" stop-color="#e11d48" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#f43f5e" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="slash-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#e11d48" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#f43f5e" stop-opacity="0"/>
    </linearGradient>

    <linearGradient id="clover-glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#e11d48" stop-opacity="0.05"/>
    </linearGradient>

    <!-- Subtle Tech Grid -->
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#38bdf8" stroke-width="0.6" stroke-opacity="0.035"/>
    </pattern>

    <filter id="glow-light" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="card-clip">
      <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14"/>
    </clipPath>
  </defs>

  <!-- Base Card Surface -->
  <rect width="{W}" height="{H}" rx="14" fill="url(#bg-grad)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#grid)"/>

  <!-- Content with Corner Clip -->
  <g clip-path="url(#card-clip)">
    <!-- Top Accent Cyber Glow Line -->
    <line x1="12" y1="1" x2="{W-12}" y2="1" stroke="url(#accent-beam)" stroke-width="2.5"/>

    <!-- Dynamic Anti-Magic Sword Slashes (Right Background) -->
    <path d="M 620 -10 L 780 155" stroke="url(#slash-grad)" stroke-width="2" stroke-dasharray="8 6" opacity="0.65"/>
    <path d="M 660 -10 L 820 155" stroke="url(#slash-grad)" stroke-width="3" opacity="0.4"/>
    <path d="M 700 -10 L 860 155" stroke="url(#slash-grad)" stroke-width="1.2" stroke-dasharray="4 8" opacity="0.5"/>

    <!-- Stylized 5-Leaf Clover Emblem (Black Clover Grimoire of the Demon) -->
    <g transform="translate(735, 72)" filter="url(#glow-light)">
      <!-- Faint Outer Circle -->
      <circle cx="0" cy="0" r="46" fill="url(#clover-glow)" stroke="#e11d48" stroke-width="1" stroke-opacity="0.35" stroke-dasharray="4 4"/>
      
      <!-- Center Stem & Core -->
      <path d="M 0 -2 C 2 -18, -2 -28, 0 -36 C 2 -28, -2 -18, 0 -2 Z" fill="#f43f5e" fill-opacity="0.7"/>
      <path d="M 2 0 C 18 2, 28 -2, 36 0 C 28 2, 18 -2, 2 0 Z" fill="#f43f5e" fill-opacity="0.7"/>
      <path d="M 0 2 C -2 18, 2 28, 0 36 C -2 28, 2 18, 0 2 Z" fill="#f43f5e" fill-opacity="0.7"/>
      <path d="M -2 0 C -18 -2, -28 2, -36 0 C -28 -2, -18 2, -2 0 Z" fill="#f43f5e" fill-opacity="0.7"/>
      <!-- The 5th Leaf (Demon Anti-Magic Leaf) -->
      <path d="M 0 0 C 12 12, 20 22, 25 30 C 18 25, 10 16, 0 0 Z" fill="#e11d48" fill-opacity="0.85"/>
      <circle cx="0" cy="0" r="4.5" fill="#f43f5e">
        <animate attributeName="r" values="3.5;5;3.5" dur="3s" repeatCount="indefinite"/>
      </circle>
    </g>

    <!-- Animated Anti-Magic & Cyber Sparks -->
    <circle cx="680" cy="45" r="1.6" fill="#38bdf8">
      <animate attributeName="opacity" values="0.2;1;0.2" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="45;35;45" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="790" cy="115" r="1.8" fill="#f43f5e">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="2.4s" begin="0.5s" repeatCount="indefinite"/>
      <animate attributeName="cy" values="115;105;115" dur="3.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="715" cy="125" r="1.2" fill="#e0f2fe">
      <animate attributeName="opacity" values="0.1;0.9;0.1" dur="1.8s" begin="1s" repeatCount="indefinite"/>
    </circle>

    <!-- Asta Quote Tagline (Right Side) -->
    <g transform="translate(645, 126)">
      <text x="0" y="0" fill="#f43f5e" font-size="9" font-weight="700" letter-spacing="1.5" text-anchor="end" opacity="0.9">❝ MY MAGIC IS NEVER GIVING UP ❞</text>
    </g>

    <!-- Left Side: Minimalist Developer Identity -->
    <!-- Category Tracking -->
    <g transform="translate(36, 34)">
      <circle cx="0" cy="-3.5" r="3" fill="#38bdf8"/>
      <text x="10" y="0" fill="#38bdf8" font-size="9.5" font-weight="700" letter-spacing="2.5">ENGINEERING ARCHITECTURES // AI &amp; SYSTEMS</text>
    </g>

    <!-- Main Title / Name -->
    <text x="36" y="68" fill="#ffffff" font-size="28" font-weight="800" letter-spacing="-0.5">Krushna Patil</text>

    <!-- Focus Subtitle -->
    <text x="36" y="93" fill="#94a3b8" font-size="12" font-weight="500" letter-spacing="0.2">
      Machine Learning <tspan fill="#38bdf8">&#183;</tspan> Deep Learning <tspan fill="#38bdf8">&#183;</tspan> Agentic AI <tspan fill="#38bdf8">&#183;</tspan> MLOps <tspan fill="#38bdf8">&#183;</tspan> Computer Vision
    </text>

    <!-- Status Indicator Pill -->
    <g transform="translate(36, 108)">
      <rect x="0" y="0" width="310" height="22" rx="11" fill="#0f172a" fill-opacity="0.8" stroke="#1e3a8a" stroke-width="1"/>
      <circle cx="12" cy="11" r="3.2" fill="#39d353">
        <animate attributeName="opacity" values="1;0.35;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="22" y="14.5" fill="#bae6fd" font-size="9" font-weight="600" letter-spacing="0.6">BUILDING AUTONOMOUS &amp; RESILIENT SYSTEMS</text>
    </g>
  </g>

  <!-- Border -->
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#334155" stroke-opacity="0.7" stroke-width="1"/>
</svg>'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out_path} ({len(svg)} bytes)")


def generate_engineering_pillars():
    """Builds the 3-column architecture cards matching reference image in Indigo/Cyan/Emerald palette."""
    out_path = os.path.join(ASSETS, "engineering-pillars.svg")
    W, H = 860, 142
    CARD_W = 264
    CARD_H = 114
    
    cards = [
        {
            "icon": "+",
            "title": "Agentic &amp; AI Systems",
            "tags": "PYTORCH &#183; MULTI-AGENT &#183; LLMS",
            "line1": "Designing autonomous agent loops, prompt contracts,",
            "line2": "and scalable model inference pipelines.",
            "card_bg": "#0e0d1f",
            "border": "#312e81",
            "badge_bg": "#1e1b4b",
            "badge_fg": "#818cf8",
            "tag_color": "#a5b4fc",
        },
        {
            "icon": "&#10003;",
            "title": "High-Performance APIs",
            "tags": "FASTAPI &#183; ASYNC &#183; NODE.JS",
            "line1": "Architecting low-latency asynchronous APIs,",
            "line2": "resilient microservices, and event queues.",
            "card_bg": "#0c1929",
            "border": "#1e3a8a",
            "badge_bg": "#172554",
            "badge_fg": "#38bdf8",
            "tag_color": "#7dd3fc",
        },
        {
            "icon": "&#9881;",
            "title": "Vision &amp; Edge Systems",
            "tags": "OPENCV &#183; TELEMETRY &#183; IOT",
            "line1": "Building real-time defect segmentation models,",
            "line2": "sensor telemetry, and predictive maintenance.",
            "card_bg": "#06231a",
            "border": "#065f46",
            "badge_bg": "#064e3b",
            "badge_fg": "#10b981",
            "tag_color": "#6ee7b7",
        }
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="\'Fira Code\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '''<style>
          .p-card { transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
          .p-card:hover { filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.35)); stroke-width: 1.5; }
        </style>''',
        f'<rect width="{W}" height="{H}" rx="12" fill="#0d1117"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#30363d" stroke-width="1"/>',
    ]

    start_x = 18
    y = 14
    for i, c in enumerate(cards):
        cx = start_x + i * (CARD_W + 17)
        parts.append(f'''
  <!-- Pillar Card {i+1} -->
  <g class="p-card" transform="translate({cx}, {y})">
    <rect width="{CARD_W}" height="{CARD_H}" rx="10" fill="{c['card_bg']}" stroke="{c['border']}" stroke-width="1"/>
    
    <!-- Badge Icon -->
    <rect x="14" y="14" width="30" height="30" rx="8" fill="{c['badge_bg']}" stroke="{c['border']}" stroke-width="1"/>
    <text x="29" y="34" fill="{c['badge_fg']}" font-size="16" font-weight="700" text-anchor="middle">{c['icon']}</text>
    
    <!-- Title & Tech Tags -->
    <text x="54" y="27" fill="#ffffff" font-size="13" font-weight="700">{c['title']}</text>
    <text x="54" y="41" fill="{c['tag_color']}" font-size="9" font-weight="700" letter-spacing="0.5">{c['tags']}</text>
    
    <!-- Description -->
    <text x="14" y="70" fill="#94a3b8" font-size="10.5" font-weight="400">
      <tspan x="14" dy="0">{c['line1']}</tspan>
      <tspan x="14" dy="16">{c['line2']}</tspan>
    </text>
  </g>''')

    parts.append('</svg>')
    svg = "".join(parts)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out_path} ({len(svg)} bytes)")


def generate_engineering_workflow():
    """Builds the 4-step engineering loop matching reference image in Indigo/Cyan/Emerald/Amber."""
    out_path = os.path.join(ASSETS, "engineering-workflow.svg")
    W, H = 860, 130
    
    steps = [
        {"num": "01 / CLARIFY", "title": "Understand the problem", "border": "#4338ca", "bg": "#1e1b4b", "accent": "#818cf8"},
        {"num": "02 / ARCHITECT", "title": "Model decoupled solutions", "border": "#0284c7", "bg": "#0c2d48", "accent": "#38bdf8"},
        {"num": "03 / BENCHMARK", "title": "Test edges &amp; latency", "border": "#059669", "bg": "#064e3b", "accent": "#10b981"},
        {"num": "04 / SHIP &amp; LOG", "title": "Deploy with telemetry", "border": "#d97706", "bg": "#451a03", "accent": "#f59e0b"},
    ]
    
    BOX_W = 175
    BOX_H = 46
    
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="\'Fira Code\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '''<style>
          .wf-box { transition: all 0.25s ease; }
          .wf-box:hover { filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.4)); stroke-width: 1.5; }
        </style>''',
        f'<rect width="{W}" height="{H}" rx="12" fill="#0d1117"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#30363d" stroke-width="1"/>',
        '<text x="24" y="28" fill="#ffffff" font-size="14.5" font-weight="700">How I approach engineering work</text>',
        '<text x="24" y="46" fill="#94a3b8" font-size="11">A systematic loop for reliable, maintainable software &amp; AI architectures</text>',
    ]

    start_x = 24
    box_y = 62
    for i, s in enumerate(steps):
        bx = start_x + i * (BOX_W + 36)
        parts.append(f'''
  <!-- Step {i+1} -->
  <g class="wf-box" transform="translate({bx}, {box_y})">
    <rect width="{BOX_W}" height="{BOX_H}" rx="8" fill="{s['bg']}" stroke="{s['border']}" stroke-width="1"/>
    <text x="12" y="18" fill="{s['accent']}" font-size="8.5" font-weight="700" letter-spacing="0.5">{s['num']}</text>
    <text x="12" y="34" fill="#ffffff" font-size="10.5" font-weight="600">{s['title']}</text>
  </g>''')
        
        # Arrow connector between steps with pulsing packet
        if i < len(steps) - 1:
            ax = bx + BOX_W + 10
            parts.append(f'''
  <g transform="translate({ax}, {box_y + 20})">
    <line x1="0" y1="0" x2="16" y2="0" stroke="#38bdf8" stroke-width="1.4" stroke-opacity="0.6"/>
    <polyline points="12,-4 16,0 12,4" fill="none" stroke="#38bdf8" stroke-width="1.4" stroke-opacity="0.6"/>
    <circle r="1.8" fill="#ffffff">
      <animateMotion path="M 0 0 L 16 0" dur="1.2s" begin="{i*0.25}s" repeatCount="indefinite"/>
    </circle>
  </g>''')

    parts.append('</svg>')
    svg = "".join(parts)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out_path} ({len(svg)} bytes)")


def generate_footer_banner():
    """Builds a clean, sleek telemetry architecture footer banner in Cyber Cyan & Slate."""
    out_path = os.path.join(ASSETS, "footer-banner.svg")
    W, H = 860, 115
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="footer-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#0d1117"/>
      <stop offset="100%" stop-color="#0b0f19"/>
    </linearGradient>
    <linearGradient id="wave-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.25"/>
      <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#6366f1" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="glow-line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
      <stop offset="30%" stop-color="#38bdf8" stop-opacity="0.85"/>
      <stop offset="70%" stop-color="#818cf8" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
    </linearGradient>
    <pattern id="footer-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#38bdf8" stroke-width="0.7" stroke-opacity="0.04"/>
    </pattern>
  </defs>

  <!-- Card Background -->
  <rect width="{W}" height="{H}" rx="14" fill="url(#footer-bg)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#footer-grid)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#30363d" stroke-width="1"/>
  
  <!-- Subtle Glowing Top Accent -->
  <line x1="60" y1="1" x2="{W-60}" y2="1" stroke="url(#glow-line)" stroke-width="2"/>

  <!-- Flowing Bottom Sine Wave Accent -->
  <path d="M 0 85 Q 215 65 430 85 T 860 85 L 860 115 L 0 115 Z" fill="url(#wave-grad)"/>
  <path d="M 0 85 Q 215 65 430 85 T 860 85" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-opacity="0.35"/>

  <!-- Architecture Quote -->
  <text x="{W/2}" y="38" fill="#f8fafc" font-size="13" font-style="italic" font-weight="500" text-anchor="middle" letter-spacing="0.3">
    &#8220;First make it work, then make it right, then make it scale &#8212; with resilient architecture at every tier.&#8221;
  </text>

  <!-- Engineering Signature & Telemetry Status -->
  <text x="{W/2}" y="62" fill="#38bdf8" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="1">
    KRUSHNA PATIL &#183; AUTONOMOUS AI &#183; HIGH-THROUGHPUT BACKENDS &#183; PUNE, INDIA
  </text>

  <!-- Pulsing Center Core Status -->
  <circle cx="{W/2}" cy="96" r="3" fill="#39d353">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="r" values="2.5;3.5;2.5" dur="2s" repeatCount="indefinite"/>
  </circle>
</svg>'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out_path} ({len(svg)} bytes)")


if __name__ == "__main__":
    generate_hero_banner()
    generate_engineering_pillars()
    generate_engineering_workflow()
    generate_footer_banner()
