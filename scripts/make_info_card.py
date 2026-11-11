"""Generate the animated AI systems visual used beside the profile portrait."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "agentic-systems.svg")

WIDTH = 980
HEIGHT = 770


def generate_card():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-labelledby="title desc">
  <title id="title">Animated agentic AI systems dashboard</title>
  <desc id="desc">A cyber-cyan animated visualization of data flowing through an AI agent network.</desc>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#08111f"/>
      <stop offset="0.55" stop-color="#0d1728"/>
      <stop offset="1" stop-color="#11133a"/>
    </linearGradient>
    <radialGradient id="core" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#e0f2fe" stop-opacity="0.95"/>
      <stop offset="0.18" stop-color="#38bdf8" stop-opacity="0.9"/>
      <stop offset="0.55" stop-color="#2563eb" stop-opacity="0.35"/>
      <stop offset="1" stop-color="#172554" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="cyan-line" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#38bdf8"/>
      <stop offset="1" stop-color="#818cf8"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#38bdf8" stroke-opacity="0.07"/>
    </pattern>
    <filter id="glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="soft-glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="2.5" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="frame"><rect x="2" y="2" width="{WIDTH - 4}" height="{HEIGHT - 4}" rx="18"/></clipPath>
  </defs>

  <rect width="{WIDTH}" height="{HEIGHT}" rx="18" fill="url(#bg)"/>
  <rect width="{WIDTH}" height="{HEIGHT}" rx="18" fill="url(#grid)"/>
  <g clip-path="url(#frame)" font-family="'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
    <path d="M0 620H980" stroke="#38bdf8" stroke-opacity="0.08"/>
    <path d="M70 0V770M910 0V770" stroke="#38bdf8" stroke-opacity="0.06"/>

    <!-- Header -->
    <text x="42" y="58" fill="#38bdf8" font-size="16" font-weight="700" letter-spacing="3">AGENTIC SYSTEMS // LIVE</text>
    <text x="42" y="91" fill="#e0f2fe" font-size="28" font-weight="700">BUILD · CONNECT · SHIP</text>
    <circle cx="900" cy="50" r="6" fill="#39d353" filter="url(#soft-glow)">
      <animate attributeName="opacity" values="1;0.25;1" dur="1.8s" repeatCount="indefinite"/>
    </circle>
    <text x="918" y="55" fill="#94a3b8" font-size="13">ONLINE</text>

    <!-- Network links -->
    <g fill="none" stroke="url(#cyan-line)" stroke-width="2" stroke-opacity="0.42">
      <path d="M490 340L230 220M490 340L750 220M490 340L190 455M490 340L790 455M490 340L300 555M490 340L680 555"/>
    </g>
    <g fill="#e0f2fe" filter="url(#soft-glow)">
      <circle r="4"><animateMotion path="M490 340L230 220" dur="2.4s" repeatCount="indefinite"/></circle>
      <circle r="4"><animateMotion path="M490 340L750 220" dur="2.9s" begin="0.4s" repeatCount="indefinite"/></circle>
      <circle r="4"><animateMotion path="M490 340L190 455" dur="2.7s" begin="0.8s" repeatCount="indefinite"/></circle>
      <circle r="4"><animateMotion path="M490 340L790 455" dur="2.2s" begin="0.2s" repeatCount="indefinite"/></circle>
      <circle r="4"><animateMotion path="M490 340L300 555" dur="2.6s" begin="0.6s" repeatCount="indefinite"/></circle>
      <circle r="4"><animateMotion path="M490 340L680 555" dur="2.5s" begin="1s" repeatCount="indefinite"/></circle>
    </g>

    <!-- Orbiting AI core -->
    <circle cx="490" cy="340" r="138" fill="none" stroke="#38bdf8" stroke-opacity="0.12" stroke-dasharray="3 12">
      <animateTransform attributeName="transform" type="rotate" from="0 490 340" to="360 490 340" dur="18s" repeatCount="indefinite"/>
    </circle>
    <circle cx="490" cy="340" r="112" fill="url(#core)" opacity="0.8" filter="url(#glow)">
      <animate attributeName="r" values="104;122;104" dur="3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.55;0.9;0.55" dur="3s" repeatCount="indefinite"/>
    </circle>
    <circle cx="490" cy="340" r="54" fill="#0b1830" stroke="#38bdf8" stroke-width="2" filter="url(#soft-glow)"/>
    <path d="M465 337h50M490 312v56M472 319l36 42M508 319l-36 42" stroke="#bae6fd" stroke-width="2" stroke-opacity="0.8"/>
    <circle cx="490" cy="340" r="10" fill="#e0f2fe">
      <animate attributeName="r" values="8;12;8" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <text x="490" y="423" fill="#bae6fd" font-size="14" text-anchor="middle" letter-spacing="2">ORCHESTRATOR</text>

    <!-- Agent nodes -->
    <g fill="#0b1830" stroke="#38bdf8" stroke-width="2">
      <circle cx="230" cy="220" r="30"/><circle cx="750" cy="220" r="30"/>
      <circle cx="190" cy="455" r="30"/><circle cx="790" cy="455" r="30"/>
      <circle cx="300" cy="555" r="30"/><circle cx="680" cy="555" r="30"/>
    </g>
    <g fill="#bae6fd" font-size="11" text-anchor="middle" font-weight="700">
      <text x="230" y="224">VISION</text><text x="750" y="224">PLANNER</text>
      <text x="190" y="459">DATA</text><text x="790" y="459">API</text>
      <text x="300" y="559">MEMORY</text><text x="680" y="559">EVAL</text>
    </g>

    <!-- Telemetry panel -->
    <rect x="42" y="650" width="896" height="76" rx="12" fill="#07101d" stroke="#1e3a8a"/>
    <text x="64" y="678" fill="#64748b" font-size="12">SYSTEM TELEMETRY</text>
    <text x="64" y="705" fill="#38bdf8" font-size="13">$ pipeline.run --mode autonomous</text>
    <text x="490" y="705" fill="#39d353" font-size="13">✓ ROUTING</text>
    <text x="620" y="705" fill="#39d353" font-size="13">✓ MEMORY</text>
    <text x="750" y="705" fill="#facc15" font-size="13">◌ EVALUATING</text>
    <rect x="825" y="669" width="82" height="4" rx="2" fill="#1e293b"/>
    <rect x="825" y="669" width="58" height="4" rx="2" fill="#38bdf8">
      <animate attributeName="width" values="24;78;42;64;24" dur="3.5s" repeatCount="indefinite"/>
    </rect>
  </g>
  <rect x="1" y="1" width="{WIDTH - 2}" height="{HEIGHT - 2}" rx="18" fill="none" stroke="#38bdf8" stroke-opacity="0.55"/>
  <rect x="3" y="3" width="{WIDTH - 6}" height="{HEIGHT - 6}" rx="16" fill="none" stroke="#30363d" stroke-opacity="0.7"/>
</svg>
"""
    with open(OUT, "w", encoding="utf-8") as file:
        file.write(svg)
    print(f"Generated {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    generate_card()
