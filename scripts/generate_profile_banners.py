"""
Generate custom red-themed engineering SVG assets for Krushna Patil's GitHub profile:
  1. assets/hero-banner.svg         - Dark crimson hero banner with architecture diagram & social strip
  2. assets/engineering-pillars.svg  - 3-column engineering focus cards (AI, Backend, Vision)
  3. assets/engineering-workflow.svg - 4-step engineering workflow loop
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")
os.makedirs(ASSETS, exist_ok=True)


def generate_hero_banner():
    """Builds the 860x250 hero banner matching Image 1 in a sleek crimson red theme."""
    out_path = os.path.join(ASSETS, "hero-banner.svg")
    W, H = 860, 245
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="card-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#14090d"/>
      <stop offset="50%" stop-color="#0e0a10"/>
      <stop offset="100%" stop-color="#0a080d"/>
    </linearGradient>
    <linearGradient id="top-accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#e63946" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#ff4d6d" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#b5179e" stop-opacity="0.4"/>
    </linearGradient>
    <pattern id="banner-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#ff4d6d" stroke-width="0.7" stroke-opacity="0.07"/>
    </pattern>
    <linearGradient id="pill-bg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#e63946"/>
      <stop offset="100%" stop-color="#d90429"/>
    </linearGradient>
  </defs>

  <!-- Card Background -->
  <rect width="{W}" height="{H}" rx="14" fill="url(#card-bg)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#banner-grid)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#3d151e" stroke-width="1"/>
  
  <!-- Subtle Top Accent Glow Line -->
  <line x1="20" y1="1" x2="{W-20}" y2="1" stroke="url(#top-accent)" stroke-width="2"/>

  <!-- Left Side: Profile & Identifiers -->
  <!-- Brain Icon Badge -->
  <rect x="32" y="26" width="36" height="36" rx="9" fill="#200d14" stroke="#4d1a24" stroke-width="1"/>
  <g transform="translate(41, 35)">
    <path d="M9 1.5 C5.5 1.5 3 4 3 7 C3 8 3.5 9 4 10 C3 11 2 12.5 2 14 C2 16.5 4 18.5 6.5 18.5 C7.5 18.5 8.5 18 9 17 C9.5 18 10.5 18.5 11.5 18.5 C14 18.5 16 16.5 16 14 C16 12.5 15 11 14 10 C14.5 9 15 8 15 7 C15 4 12.5 1.5 9 1.5 Z" fill="none" stroke="#ff4d6d" stroke-width="1.3"/>
    <line x1="9" y1="3" x2="9" y2="16.5" stroke="#ff4d6d" stroke-width="1.2" stroke-dasharray="2 2"/>
  </g>

  <!-- Plus-Minus Symbol Badge -->
  <rect x="76" y="26" width="36" height="36" rx="9" fill="#260f18" stroke="#5a1e2b" stroke-width="1"/>
  <text x="94" y="49" fill="#ff758f" font-size="18" font-weight="700" text-anchor="middle">&#177;</text>

  <!-- Main Name & Subtitles -->
  <text x="34" y="85" fill="#ff758f" font-size="10.5" font-weight="700" letter-spacing="2">ENGINEERING PROFILE</text>
  <text x="34" y="117" fill="#ffffff" font-size="27" font-weight="800" letter-spacing="-0.5">Krushna Patil</text>
  <text x="34" y="141" fill="#cbd5e1" font-size="12.5" font-weight="500">Full Stack AIML &middot; Agentic AI &middot; PyTorch &middot; High-Throughput Systems</text>

  <!-- Open to Roles Pill -->
  <rect x="34" y="156" width="335" height="24" rx="12" fill="#220e16" stroke="#4a1924" stroke-width="1"/>
  <circle cx="48" cy="168" r="3.5" fill="#e63946">
    <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
  </circle>
  <text x="59" y="172.5" fill="#fecdd3" font-size="10" font-weight="600" letter-spacing="0.5">OPEN TO SOFTWARE ENGINEERING &amp; AIML ROLES</text>

  <!-- Right Side: Architecture Flow & Taglines -->
  <g transform="translate(510, 32)">
    <!-- Circuit Architecture Flow Diagram with Animated Packets -->
    <rect x="0" y="0" width="56" height="22" rx="6" fill="#1e0b12" stroke="#e63946" stroke-width="1"/>
    <text x="28" y="14.5" fill="#fecdd3" font-size="9" font-weight="700" text-anchor="middle">INGEST</text>

    <!-- Wire: Ingest -> Agent -->
    <line x1="56" y1="11" x2="74" y2="11" stroke="#ff4d6d" stroke-width="1.2"/>
    <circle r="1.8" fill="#ff758f">
      <animateMotion path="M 56 11 L 74 11" dur="1.4s" repeatCount="indefinite"/>
    </circle>

    <rect x="74" y="0" width="58" height="22" rx="6" fill="#1e0b12" stroke="#e63946" stroke-width="1"/>
    <text x="103" y="14.5" fill="#fecdd3" font-size="9" font-weight="700" text-anchor="middle">AGENT</text>

    <!-- Branch Wires -->
    <path id="flow-top" d="M 132 11 L 144 5 L 156 5" fill="none" stroke="#ff4d6d" stroke-width="1.2"/>
    <circle r="1.8" fill="#ffffff">
      <animateMotion path="M 132 11 L 144 5 L 156 5" dur="1.8s" repeatCount="indefinite"/>
    </circle>

    <path id="flow-bot" d="M 132 11 L 144 17 L 156 17" fill="none" stroke="#ff4d6d" stroke-width="1.2"/>
    <circle r="1.8" fill="#ff4d6d">
      <animateMotion path="M 132 11 L 144 17 L 156 17" dur="1.8s" begin="0.3s" repeatCount="indefinite"/>
    </circle>

    <rect x="156" y="-3" width="70" height="15" rx="4" fill="#290e18" stroke="#ff4d6d" stroke-width="1"/>
    <text x="191" y="8" fill="#ff758f" font-size="8" font-weight="700" text-anchor="middle">LLM / RAG</text>

    <rect x="156" y="13" width="70" height="15" rx="4" fill="#290e18" stroke="#ff4d6d" stroke-width="1"/>
    <text x="191" y="24" fill="#ff758f" font-size="8" font-weight="700" text-anchor="middle">MODEL</text>

    <!-- Convergence Wires -->
    <path d="M 226 5 L 238 5 L 246 11" fill="none" stroke="#ff4d6d" stroke-width="1.2"/>
    <path d="M 226 20 L 238 20 L 246 11" fill="none" stroke="#ff4d6d" stroke-width="1.2"/>
    <circle r="1.8" fill="#ffffff">
      <animateMotion path="M 226 5 L 238 5 L 256 11" dur="1.6s" begin="0.6s" repeatCount="indefinite"/>
    </circle>

    <circle cx="270" cy="11" r="14" fill="#220b13" stroke="#e63946" stroke-width="1.2"/>
    <text x="270" y="14.5" fill="#ffffff" font-size="8.5" font-weight="700" text-anchor="middle">DEPLOY</text>

    <!-- Sub-node CI/OPS -->
    <circle cx="304" cy="25" r="11" fill="#19070e" stroke="#ff4d6d" stroke-width="0.9"/>
    <text x="304" y="28" fill="#ff758f" font-size="7.5" font-weight="700" text-anchor="middle">OPS</text>
    <line x1="284" y1="13" x2="294" y2="20" stroke="#ff4d6d" stroke-width="1"/>
    <circle r="1.5" fill="#ff4d6d">
      <animateMotion path="M 284 13 L 294 20" dur="1.5s" repeatCount="indefinite"/>
    </circle>

    <!-- Right Header -->
    <text x="315" y="70" fill="#94a3b8" font-size="9" font-weight="700" letter-spacing="1" text-anchor="end">DESIGNING SYSTEMS THAT ARE</text>
    <text x="315" y="93" fill="#ffffff" font-size="14.5" font-weight="700" text-anchor="end">
      <tspan fill="#ff4d6d">autonomous</tspan> &middot; <tspan fill="#ffffff">scalable</tspan> &middot; <tspan fill="#f43f5e">resilient</tspan>
    </text>

    <!-- Building in Public Status -->
    <circle cx="195" cy="120" r="3.5" fill="#e63946">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text x="206" y="123.5" fill="#cbd5e1" font-size="9.5" font-weight="600" letter-spacing="0.5">BUILDING IN PUBLIC</text>
  </g>

  <!-- Bottom Badges Strip -->
  <g transform="translate(34, 196)">
    <!-- GitHub Pill -->
    <rect x="0" y="0" width="105" height="26" rx="6" fill="#1e242c"/>
    <path d="M 18 13 C 18 9.7 15.3 7 12 7 C 8.7 7 6 9.7 6 13 C 6 15.6 7.7 17.8 10.1 18.6 C 10.4 18.7 10.5 18.5 10.5 18.3 L 10.5 17.2 C 8.8 17.6 8.5 16.4 8.5 16.4 C 8.2 15.7 7.8 15.5 7.8 15.5 C 7.3 15.1 7.9 15.1 7.9 15.1 C 8.5 15.2 8.8 15.7 8.8 15.7 C 9.3 16.7 10.3 16.4 10.6 16.2 C 10.7 15.8 10.8 15.5 11 15.3 C 9.7 15.1 8.3 14.6 8.3 12.3 C 8.3 11.6 8.5 11.1 9 10.7 C 8.9 10.5 8.7 9.8 9.1 9 C 9.1 9 9.6 8.8 10.8 9.6 C 11.3 9.5 11.8 9.4 12.3 9.4 C 12.8 9.4 13.3 9.5 13.8 9.6 C 15 8.8 15.5 9 15.5 9 C 15.9 9.8 15.7 10.5 15.6 10.7 C 16.1 11.1 16.3 11.6 16.3 12.3 C 16.3 14.6 14.9 15.1 13.6 15.3 C 13.8 15.5 14 15.9 14 16.5 L 14 18.3 C 14 18.5 14.1 18.7 14.5 18.6 C 16.9 17.8 18.6 15.6 18.6 13 Z" fill="#ffffff" transform="scale(0.85) translate(4, 2)"/>
    <text x="34" y="17" fill="#ffffff" font-size="10" font-weight="700">GITHUB</text>

    <!-- Username Pill (Crimson) -->
    <rect x="108" y="0" width="165" height="26" rx="6" fill="#130a0e" stroke="#4a1822" stroke-width="1"/>
    <text x="190" y="17" fill="#ff758f" font-size="10.5" font-weight="700" text-anchor="middle">KRISHNA009-PRO</text>

    <!-- Email Label Pill -->
    <rect x="281" y="0" width="85" height="26" rx="6" fill="#1e242c"/>
    <text x="300" y="17" fill="#e63946" font-size="12" font-weight="900">&#9993;</text>
    <text x="318" y="17" fill="#ffffff" font-size="10" font-weight="700">EMAIL</text>

    <!-- Email Value Pill (Bright Red) -->
    <rect x="369" y="0" width="220" height="26" rx="6" fill="url(#pill-bg)"/>
    <text x="479" y="17" fill="#ffffff" font-size="10" font-weight="700" text-anchor="middle">KKP1882006@GMAIL.COM</text>

    <!-- Location Pill -->
    <rect x="597" y="0" width="85" height="26" rx="6" fill="#1e242c"/>
    <text x="612" y="17" fill="#ff4d6d" font-size="11">&#9873;</text>
    <text x="626" y="17" fill="#ffffff" font-size="10" font-weight="700">PUNE</text>

    <!-- Country Pill -->
    <rect x="685" y="0" width="75" height="26" rx="6" fill="#240f17" stroke="#5c1d29" stroke-width="1"/>
    <text x="722" y="17" fill="#ff758f" font-size="10" font-weight="700" text-anchor="middle">INDIA</text>
  </g>
</svg>'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out_path} ({len(svg)} bytes)")


def generate_engineering_pillars():
    """Builds the 3-column architecture cards matching Image 2 in crimson red theme."""
    out_path = os.path.join(ASSETS, "engineering-pillars.svg")
    W, H = 860, 142
    CARD_W = 264
    CARD_H = 114
    
    cards = [
        {
            "icon": "+",
            "title": "Agentic & AI Systems",
            "tags": "PYTORCH &middot; MULTI-AGENT &middot; LLMS",
            "line1": "Designing autonomous agent loops, prompt contracts,",
            "line2": "and scalable model inference pipelines.",
            "border": "#541b25",
            "badge_bg": "#2e0f16",
            "badge_fg": "#ff4d6d",
        },
        {
            "icon": "&#10003;",
            "title": "High-Performance APIs",
            "tags": "FASTAPI &middot; ASYNC &middot; NODE.JS",
            "line1": "Architecting low-latency asynchronous APIs,",
            "line2": "resilient microservices, and event queues.",
            "border": "#541b25",
            "badge_bg": "#2e0f16",
            "badge_fg": "#ff4d6d",
        },
        {
            "icon": "&#9881;",
            "title": "Vision & Edge Systems",
            "tags": "OPENCV &middot; TELEMETRY &middot; IOT",
            "line1": "Building real-time defect segmentation models,",
            "line2": "sensor telemetry, and predictive maintenance.",
            "border": "#541b25",
            "badge_bg": "#2e0f16",
            "badge_fg": "#ff4d6d",
        }
    ]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="\'Fira Code\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '''<style>
          .p-card { transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); }
          .p-card:hover { filter: drop-shadow(0 0 12px rgba(230, 57, 70, 0.45)); stroke: #ff4d6d; }
        </style>''',
        f'<rect width="{W}" height="{H}" rx="12" fill="#0c090e"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#2a1218" stroke-width="1"/>',
    ]

    start_x = 18
    y = 14
    for i, c in enumerate(cards):
        cx = start_x + i * (CARD_W + 17)
        parts.append(f'''
  <!-- Pillar Card {i+1} -->
  <g class="p-card" transform="translate({cx}, {y})">
    <rect width="{CARD_W}" height="{CARD_H}" rx="10" fill="#13090e" stroke="{c['border']}" stroke-width="1"/>
    
    <!-- Badge Icon -->
    <rect x="14" y="14" width="30" height="30" rx="8" fill="{c['badge_bg']}" stroke="#521b25" stroke-width="1"/>
    <text x="29" y="34" fill="{c['badge_fg']}" font-size="16" font-weight="700" text-anchor="middle">{c['icon']}</text>
    
    <!-- Title & Tech Tags -->
    <text x="54" y="27" fill="#ffffff" font-size="13" font-weight="700">{c['title']}</text>
    <text x="54" y="41" fill="#ff758f" font-size="9" font-weight="700" letter-spacing="0.5">{c['tags']}</text>
    
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
    """Builds the 4-step engineering loop matching Image 3 in crimson red theme."""
    out_path = os.path.join(ASSETS, "engineering-workflow.svg")
    W, H = 860, 130
    
    steps = [
        {"num": "01 / CLARIFY", "title": "Understand the problem", "border": "#e63946", "bg": "#1c0b11"},
        {"num": "02 / ARCHITECT", "title": "Model decoupled solutions", "border": "#ff4d6d", "bg": "#170a10"},
        {"num": "03 / BENCHMARK", "title": "Test edges & latency", "border": "#ff758f", "bg": "#170a10"},
        {"num": "04 / SHIP & LOG", "title": "Deploy with telemetry", "border": "#fb7185", "bg": "#170a10"},
    ]
    
    BOX_W = 175
    BOX_H = 46
    
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="\'Fira Code\', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">',
        '''<style>
          .wf-box { transition: all 0.25s ease; }
          .wf-box:hover { filter: drop-shadow(0 0 8px rgba(255, 77, 109, 0.4)); stroke-width: 1.5; }
        </style>''',
        f'<rect width="{W}" height="{H}" rx="12" fill="#0c090e"/>',
        f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#2a1218" stroke-width="1"/>',
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
    <text x="12" y="18" fill="{s['border']}" font-size="8.5" font-weight="700" letter-spacing="0.5">{s['num']}</text>
    <text x="12" y="34" fill="#ffffff" font-size="10.5" font-weight="600">{s['title']}</text>
  </g>''')
        
        # Arrow connector between steps with pulsing packet
        if i < len(steps) - 1:
            ax = bx + BOX_W + 10
            parts.append(f'''
  <g transform="translate({ax}, {box_y + 20})">
    <line x1="0" y1="0" x2="16" y2="0" stroke="#e63946" stroke-width="1.4" stroke-opacity="0.6"/>
    <polyline points="12,-4 16,0 12,4" fill="none" stroke="#e63946" stroke-width="1.4" stroke-opacity="0.6"/>
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
    """Builds a luxury crimson red footer banner with quote, accent wave, and engineering signature."""
    out_path = os.path.join(ASSETS, "footer-banner.svg")
    W, H = 860, 115
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <defs>
    <linearGradient id="footer-bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#14090d"/>
      <stop offset="50%" stop-color="#0e0a10"/>
      <stop offset="100%" stop-color="#0a080d"/>
    </linearGradient>
    <linearGradient id="wave-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#e63946" stop-opacity="0.35"/>
      <stop offset="50%" stop-color="#ff4d6d" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#b5179e" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="glow-line" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#e63946" stop-opacity="0"/>
      <stop offset="30%" stop-color="#ff4d6d" stop-opacity="0.85"/>
      <stop offset="70%" stop-color="#ff758f" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#e63946" stop-opacity="0"/>
    </linearGradient>
    <pattern id="footer-grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#ff4d6d" stroke-width="0.7" stroke-opacity="0.05"/>
    </pattern>
  </defs>

  <!-- Card Background -->
  <rect width="{W}" height="{H}" rx="14" fill="url(#footer-bg)"/>
  <rect width="{W}" height="{H}" rx="14" fill="url(#footer-grid)"/>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="#3d151e" stroke-width="1"/>
  
  <!-- Subtle Glowing Top Accent -->
  <line x1="60" y1="1" x2="{W-60}" y2="1" stroke="url(#glow-line)" stroke-width="2"/>

  <!-- Flowing Bottom Sine Wave Accent -->
  <path d="M 0 85 Q 215 65 430 85 T 860 85 L 860 115 L 0 115 Z" fill="url(#wave-grad)"/>
  <path d="M 0 85 Q 215 65 430 85 T 860 85" fill="none" stroke="#ff4d6d" stroke-width="1.2" stroke-opacity="0.45"/>

  <!-- Inspirational Architecture Quote -->
  <text x="{W/2}" y="38" fill="#f8fafc" font-size="13" font-style="italic" font-weight="500" text-anchor="middle" letter-spacing="0.3">
    &ldquo;First make it work, then make it right, then make it scale &mdash; with resilient architecture at every tier.&rdquo;
  </text>

  <!-- Engineering Signature & Telemetry Status -->
  <text x="{W/2}" y="62" fill="#ff758f" font-size="10.5" font-weight="700" text-anchor="middle" letter-spacing="1">
    KRUSHNA PATIL &middot; AUTONOMOUS AI &middot; HIGH-THROUGHPUT BACKENDS &middot; PUNE, INDIA
  </text>

  <!-- Pulsing Center Core Status -->
  <circle cx="{W/2}" cy="96" r="3" fill="#e63946">
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
