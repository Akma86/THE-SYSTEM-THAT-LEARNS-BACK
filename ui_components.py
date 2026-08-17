import streamlit as st
import matplotlib.pyplot as plt

# ==============================================================================
# GLOBAL CYBERPUNK DESIGN SYSTEM
# ==============================================================================
GLOBAL_THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Barlow+Condensed:wght@600;700;800;900&family=JetBrains+Mono:wght@400;500;700&family=Outfit:wght@400;600;700;800;900&display=swap');

/* Master root variables */
:root {
    --bg-dark: #030712;
    --bg-card: rgba(15, 23, 42, 0.65);
    --bg-card-hover: rgba(30, 41, 59, 0.75);
    --border-subtle: rgba(148, 163, 184, 0.12);
    --border-glow: rgba(56, 189, 248, 0.3);
    --accent-cyan: #06b6d4;
    --accent-emerald: #10b981;
    --accent-amber: #f59e0b;
    --accent-purple: #8b5cf6;
    --accent-rose: #f43f5e;
    --accent-orange: #f97316;
    --text-main: #f8fafc;
    --text-muted: #94a3b8;
    --text-dim: #64748b;
}

/* Global Reset & Base Styling */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #030712;
    color: #f8fafc;
    -webkit-font-smoothing: antialiased;
}

/* App Background with Multi-Layer Ambient Glow */
.stApp {
    background:
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(37, 99, 235, 0.18), transparent 70%),
        radial-gradient(circle at 10% 20%, rgba(16, 185, 129, 0.08), transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(139, 92, 246, 0.12), transparent 45%),
        radial-gradient(circle at 50% 90%, rgba(244, 63, 94, 0.06), transparent 50%),
        linear-gradient(180deg, #020617 0%, #030712 50%, #050b14 100%);
    background-attachment: fixed;
    overflow-x: hidden;
}

/* Streamlit defaults cleanup */
#MainMenu { visibility: hidden !important; }
footer { visibility: hidden !important; }
header { visibility: hidden !important; }

/* Container width & padding */
.block-container {
    max-width: 1240px;
    padding-top: 1.5rem !important;
    padding-bottom: 5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ==============================================================================
   CYBER HUD / NAVIGATION BAR
   ============================================================================== */
.cyber-hud {
    background: rgba(10, 16, 30, 0.85);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 20px;
    padding: 14px 24px;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 12px;
    backdrop-filter: blur(20px);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.45), inset 0 0 20px rgba(56, 189, 248, 0.04);
}

.hud-left {
    display: flex;
    align-items: center;
    gap: 14px;
}

.hud-badge-logo {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: 'Space Mono', monospace;
    font-weight: 700;
    font-size: 0.85rem;
    letter-spacing: 1.5px;
    color: #38bdf8;
    background: rgba(56, 189, 248, 0.1);
    padding: 6px 14px;
    border-radius: 10px;
    border: 1px solid rgba(56, 189, 248, 0.25);
    text-transform: uppercase;
}

.hud-status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 10px #10b981, 0 0 20px #10b981;
    animation: hudPulse 2s infinite ease-in-out;
}

@keyframes hudPulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(1.3); }
}

.hud-clearance {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 1.5px;
    color: #e2e8f0;
    text-transform: uppercase;
}

.hud-clearance span {
    color: #f43f5e;
    font-weight: 700;
}

.hud-stages-track {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(2, 6, 23, 0.7);
    padding: 6px 12px;
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.stage-pill {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 1px;
    padding: 4px 10px;
    border-radius: 8px;
    color: #64748b;
    border: 1px solid transparent;
    transition: all 0.3s ease;
}

.stage-pill.active {
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.35), rgba(124, 58, 237, 0.35));
    border-color: rgba(56, 189, 248, 0.5);
    color: #38bdf8;
    font-weight: 700;
    box-shadow: 0 0 12px rgba(56, 189, 248, 0.25);
}

.stage-pill.done {
    background: rgba(16, 185, 129, 0.12);
    border-color: rgba(16, 185, 129, 0.3);
    color: #10b981;
}

/* ==============================================================================
   GLASS CARD CONTAINERS
   ============================================================================== */
.glass-card {
    position: relative;
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.7) 0%, rgba(2, 6, 23, 0.8) 100%);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 28px;
    padding: 2.75rem 3rem;
    backdrop-filter: blur(24px);
    -webkit-backdrop-filter: blur(24px);
    box-shadow:
        0 20px 50px rgba(0, 0, 0, 0.5),
        inset 0 1px 0 rgba(255, 255, 255, 0.1),
        inset 0 0 20px rgba(255, 255, 255, 0.02);
    margin-bottom: 2.5rem;
    overflow: hidden;
    animation: fadeInUp 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}

.glass-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent 0%, rgba(56, 189, 248, 0.5) 50%, transparent 100%);
    opacity: 0.7;
}

.glass-card.hero {
    text-align: center;
}

.main-title {
    font-family: 'Outfit', sans-serif;
    font-size: 4.2rem;
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -2px;
    margin-bottom: 0.75rem;
    text-align: center;
    background: linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 50%, #94A3B8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 20px rgba(255, 255, 255, 0.15));
}

.subtitle {
    text-align: center;
    font-family: 'Space Mono', monospace;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 6px;
    color: #38bdf8;
    margin-bottom: 2.5rem;
    opacity: 0.9;
}

.section-title {
    font-family: 'Outfit', sans-serif;
    text-align: center;
    font-size: 1.85rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-bottom: 1.75rem;
    color: #f8fafc;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
}

.story-text {
    max-width: 800px;
    margin: auto;
    text-align: center;
    line-height: 2.2;
    font-size: 1.08rem;
    font-weight: 400;
    color: #cbd5e1;
    white-space: pre-line;
}

.story-text b, .story-text strong {
    color: #ffffff;
    font-weight: 700;
    text-shadow: 0 0 16px rgba(255, 255, 255, 0.25);
}

/* Divider */
hr {
    border: none;
    height: 1px;
    width: 65%;
    margin: 2.5rem auto;
    background: linear-gradient(
        90deg,
        transparent 0%,
        rgba(56, 189, 248, 0.1) 15%,
        rgba(56, 189, 248, 0.4) 50%,
        rgba(56, 189, 248, 0.1) 85%,
        transparent 100%
    );
    box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
    opacity: 0.8;
}

/* ==============================================================================
   TERMINAL & CODE CARDS
   ============================================================================== */
.terminal {
    background: #020617;
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 20px;
    padding: 2rem 2.25rem;
    max-width: 840px;
    margin: 1.5rem auto;
    box-shadow:
        inset 0 0 35px rgba(56, 189, 248, 0.04),
        0 10px 30px rgba(0, 0, 0, 0.5);
    font-family: 'JetBrains Mono', 'Space Mono', monospace;
    color: #67e8f9;
    line-height: 2;
    font-size: 0.96rem;
    position: relative;
    overflow: hidden;
}

.terminal::before {
    content: "SYS_LOG // TERMINAL OUTPUT";
    position: absolute;
    top: 8px;
    right: 18px;
    font-size: 0.65rem;
    letter-spacing: 2px;
    color: rgba(56, 189, 248, 0.4);
}

.terminal-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid rgba(56, 189, 248, 0.15);
}

.term-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
}
.term-dot.red { background: #ef4444; }
.term-dot.yellow { background: #f59e0b; }
.term-dot.green { background: #10b981; }

.terminal-title {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 2px;
    color: #94a3b8;
    text-transform: uppercase;
    margin-left: 6px;
}

/* ==============================================================================
   STREAMLIT FORM WIDGETS & BUTTONS
   ============================================================================== */
/* Text inputs */
.stTextInput > div > div > input {
    background: rgba(15, 23, 42, 0.6) !important;
    border: 1px solid rgba(56, 189, 248, 0.25) !important;
    border-radius: 16px !important;
    color: #ffffff !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 1.05rem !important;
    padding: 16px 20px !important;
    text-align: center !important;
    letter-spacing: 1px !important;
    transition: all 0.3s ease !important;
    box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.4) !important;
}

.stTextInput > div > div > input:focus {
    border-color: #38bdf8 !important;
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.35), inset 0 2px 8px rgba(0, 0, 0, 0.4) !important;
    background: rgba(15, 23, 42, 0.9) !important;
}

.stTextInput label {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.88rem !important;
    letter-spacing: 1.5px !important;
    color: #94a3b8 !important;
    text-transform: uppercase !important;
    margin-bottom: 8px !important;
}

/* Buttons */
.stButton > button {
    width: 100% !important;
    min-height: 56px !important;
    border-radius: 18px !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    font-family: 'Outfit', 'Inter', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    letter-spacing: 0.8px !important;
    color: #ffffff !important;
    background: linear-gradient(135deg, #2563eb 0%, #7c3aed 50%, #db2777 100%) !important;
    box-shadow: 0 8px 25px rgba(124, 58, 237, 0.35) !important;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
    cursor: pointer !important;
    margin-top: 10px !important;
    text-transform: uppercase !important;
}

.stButton > button:hover {
    transform: translateY(-3px) scale(1.01) !important;
    box-shadow: 0 12px 35px rgba(124, 58, 237, 0.55), 0 0 20px rgba(56, 189, 248, 0.35) !important;
    border-color: rgba(255, 255, 255, 0.3) !important;
}

.stButton > button:active {
    transform: translateY(0px) scale(0.99) !important;
}

/* Alert Boxes */
.stAlert {
    border-radius: 18px !important;
    backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    font-family: 'Inter', sans-serif !important;
}

.stDataFrame, .stTable {
    border-radius: 18px !important;
    overflow: hidden !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    background: rgba(10, 16, 30, 0.5) !important;
}

/* Radio buttons & Expander */
.stRadio > div {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
}

div[data-testid="stExpander"] {
    background: rgba(15, 23, 42, 0.5) !important;
    border: 1px solid rgba(56, 189, 248, 0.2) !important;
    border-radius: 18px !important;
    margin-bottom: 1rem !important;
}

/* Stat Grid */
.stat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin: 1.5rem 0;
}

.stat-box {
    background: rgba(2, 6, 23, 0.6);
    border: 1px solid rgba(56, 189, 248, 0.18);
    border-radius: 18px;
    padding: 18px 20px;
    text-align: center;
    backdrop-filter: blur(10px);
}

.stat-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 2px;
    color: #94a3b8;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.stat-value {
    font-family: 'Barlow Condensed', 'Outfit', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: #f8fafc;
    line-height: 1;
}

.stat-value.cyan { color: #38bdf8; }
.stat-value.emerald { color: #34d399; }
.stat-value.amber { color: #fbbf24; }
.stat-value.rose { color: #fb7185; }

/* Keyframe animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(24px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 768px) {
    .main-title { font-size: 2.8rem; letter-spacing: -1px; }
    .glass-card { padding: 1.75rem 1.25rem; }
    .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
    .cyber-hud { flex-direction: column; align-items: flex-start; }
}
</style>
"""


# ==============================================================================
# HUD COMPONENT
# ==============================================================================
def render_cyber_hud(current_stage: int):
    """Renders the top cyber investigation HUD."""
    stages_info = [
        (0, "INTRO", "00"),
        (1, "NOISE", "01"),
        (2, "CONVERGENCE", "02"),
        (3, "ACCESS", "03"),
        (4, "EXTRACTION", "04"),
        (5, "FINISH", "05"),
        (6, "SYSTEM", "06"),
    ]

    pills_html = ""
    for s_idx, s_name, s_code in stages_info:
        if s_idx == current_stage:
            cls = "stage-pill active"
        elif s_idx < current_stage:
            cls = "stage-pill done"
        else:
            cls = "stage-pill"
        pills_html += f'<div class="{cls}">{s_code} {s_name}</div>'

    clearance_levels = {
        0: "OBSERVER [LVL 0]",
        1: "ANALYST [LVL 1]",
        2: "SPECIALIST [LVL 2]",
        3: "ROOT OPERATOR [LVL 3]",
        4: "CYBER AGENT [LVL 4]",
        5: "DEEP AUDITOR [LVL 5]",
        6: "COMPROMISED [SYS]",
        7: "ARCHIVE VIEWER",
    }
    clearance = clearance_levels.get(current_stage, "INVESTIGATOR")

    hud_html = f"""
    <div class="cyber-hud">
        <div class="hud-left">
            <div class="hud-badge-logo">
                <div class="hud-status-dot"></div>
                FINCORE::SHADOW
            </div>
            <div class="hud-clearance">CLEARANCE: <span>{clearance}</span></div>
        </div>
        <div class="hud-stages-track">
            {pills_html}
        </div>
    </div>
    """
    st.markdown(hud_html, unsafe_allow_html=True)


# ==============================================================================
# BANNER COMPONENT
# ==============================================================================
def render_stage_banner(
    stage_num: str,
    chapter_num: str,
    title_line1: str,
    title_line2: str,
    accent_color: str,
    meta_tags: list,
    ticker_items: list,
    node_name: str = "NODE_SYS",
    status_label: str = "RESTRICTED",
):
    """Renders a purely CSS-animated stage banner that avoids Streamlit JS sanitization issues."""
    meta_spans = " · ".join([f"<span>{tag}</span>" for tag in meta_tags])

    ticker_spans = ""
    for item in ticker_items:
        hot_cls = "hot" if item.get("hot") else ("warn" if item.get("warn") else "")
        ticker_spans += f'<span class="sb-tick-item {hot_cls}">{item["text"]}</span>'
    # Duplicate for smooth infinite loop
    ticker_spans_full = ticker_spans + ticker_spans

    banner_html = f"""
    <style>
      .sb-root-{stage_num} {{
        font-family: 'Space Mono', monospace;
        background: #020712;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        overflow: hidden;
        position: relative;
        width: 100%;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5), inset 0 0 30px {accent_color}10;
      }}
      .sb-topbar-{stage_num} {{
        display: flex; align-items: center; justify-content: space-between;
        padding: 8px 18px; border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(2,6,23,0.85);
      }}
      .sb-dot-{stage_num} {{
        width: 8px; height: 8px; border-radius: 50%; background: {accent_color};
        box-shadow: 0 0 12px {accent_color};
        animation: sb-pulse-{stage_num} 1.8s infinite;
      }}
      @keyframes sb-pulse-{stage_num} {{
        0%,100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(1.3); }}
      }}
      .sb-main-{stage_num} {{
        position: relative; height: 230px; overflow: hidden;
        display: flex; align-items: stretch;
        background: linear-gradient(135deg, rgba(2,6,23,0.95), rgba(15,23,42,0.85));
      }}
      .sb-scanline-{stage_num} {{
        position: absolute; left: 0; right: 0; height: 2px;
        background: linear-gradient(90deg, transparent 0%, {accent_color}40 20%, {accent_color}90 50%, {accent_color}40 80%, transparent 100%);
        animation: sb-scan-{stage_num} 3.5s linear infinite; pointer-events: none; z-index: 5;
      }}
      @keyframes sb-scan-{stage_num} {{
        0% {{ top: -2px; }}
        100% {{ top: 230px; }}
      }}
      .sb-left-bar-{stage_num} {{
        width: 4px; background: {accent_color}; flex-shrink: 0; position: relative; z-index: 2;
        box-shadow: 0 0 15px {accent_color};
      }}
      .sb-vert-label-{stage_num} {{
        writing-mode: vertical-rl; transform: rotate(180deg); font-size: 11px;
        letter-spacing: 3px; color: {accent_color}; opacity: 0.7; text-transform: uppercase;
        padding: 12px 10px; flex-shrink: 0; position: relative; z-index: 2;
        border-right: 1px solid rgba(255,255,255,0.06);
      }}
      .sb-center-{stage_num} {{
        flex: 1; display: flex; flex-direction: column; justify-content: center;
        padding: 0 28px; position: relative; z-index: 2;
      }}
      .sb-chapter-{stage_num} {{
        font-size: 13px; letter-spacing: 4px; color: {accent_color}; opacity: 0.9;
        text-transform: uppercase; margin-bottom: 6px;
        display: flex; align-items: center; gap: 8px; font-weight: 700;
      }}
      .sb-title-{stage_num} {{
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 64px;
        line-height: 0.92; letter-spacing: -1.5px; color: #f8fafc;
        text-transform: uppercase; margin-bottom: 10px;
      }}
      .sb-title-{stage_num} span {{ color: {accent_color}; display: block; }}
      .sb-meta-{stage_num} {{
        font-size: 11px; letter-spacing: 1.5px; color: #94a3b8;
        text-transform: uppercase; display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
      }}
      .sb-right-{stage_num} {{
        display: flex; flex-direction: column; align-items: flex-end;
        justify-content: center; padding: 0 24px; gap: 8px;
        position: relative; z-index: 2; border-left: 1px solid rgba(255,255,255,0.06);
      }}
      .sb-hex-{stage_num} {{
        font-family: 'Barlow Condensed', sans-serif; font-weight: 900; font-size: 80px;
        line-height: 1; color: {accent_color}; opacity: 0.12; letter-spacing: -3px;
      }}
      .sb-badge-{stage_num} {{
        font-size: 11px; letter-spacing: 2px; padding: 4px 12px;
        border: 1px solid {accent_color}80; color: {accent_color};
        text-transform: uppercase; margin-top: -24px; border-radius: 6px;
        background: {accent_color}15;
      }}
      .sb-bottombar-{stage_num} {{
        display: flex; align-items: stretch;
        border-top: 1px solid rgba(255,255,255,0.06); background: rgba(2,6,23,0.9);
      }}
      .sb-ticker-wrap-{stage_num} {{ flex: 1; overflow: hidden; position: relative; }}
      .sb-ticker-{stage_num} {{
        display: flex; align-items: center; gap: 0;
        animation: sb-tick-{stage_num} 24s linear infinite; white-space: nowrap; padding: 8px 0;
      }}
      @keyframes sb-tick-{stage_num} {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-50%); }}
      }}
      .sb-tick-item {{
        font-size: 11px; letter-spacing: 1.5px; color: #64748b; text-transform: uppercase;
        padding: 0 18px; border-right: 1px solid rgba(255,255,255,0.06); flex-shrink: 0;
      }}
      .sb-tick-item.hot {{ color: {accent_color}; font-weight: 700; }}
      .sb-tick-item.warn {{ color: #f59e0b; }}
    </style>

    <div class="sb-root-{stage_num}">
      <div class="sb-topbar-{stage_num}">
        <div style="display:flex; align-items:center; gap:10px;">
          <div class="sb-dot-{stage_num}"></div>
          <span style="font-size:11px; letter-spacing:2px; color:{accent_color}; opacity:0.85;">
            SYS::FINCORE · {node_name} · MONITORING ACTIVE
          </span>
        </div>
        <span style="font-size:10px; letter-spacing:2px; color:#f43f5e; border:1px solid #f43f5e60; padding:2px 8px; border-radius:4px;">
          {status_label}
        </span>
      </div>

      <div class="sb-main-{stage_num}">
        <div class="sb-scanline-{stage_num}"></div>
        <div class="sb-left-bar-{stage_num}"></div>
        <div class="sb-vert-label-{stage_num}">Stage {stage_num}</div>
        <div class="sb-center-{stage_num}">
          <div class="sb-chapter-{stage_num}">Chapter {chapter_num}</div>
          <div class="sb-title-{stage_num}">
            {title_line1}
            <span>{title_line2}</span>
          </div>
          <div class="sb-meta-{stage_num}">
            {meta_spans}
          </div>
        </div>
        <div class="sb-right-{stage_num}">
          <div class="sb-hex-{stage_num}">{stage_num}</div>
          <div class="sb-badge-{stage_num}">LIVE TELEMETRY</div>
        </div>
      </div>

      <div class="sb-bottombar-{stage_num}">
        <div class="sb-ticker-wrap-{stage_num}">
          <div class="sb-ticker-{stage_num}">
            {ticker_spans_full}
          </div>
        </div>
      </div>
    </div>
    """
    st.markdown(banner_html, unsafe_allow_html=True)


# ==============================================================================
# MATPLOTLIB STYLING HELPER
# ==============================================================================
def apply_cyber_plot_style(fig, ax, bg_color="#060B14"):
    """Applies a crisp dark cyberpunk theme to matplotlib charts."""
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)
    ax.tick_params(colors="#94A3B8", labelsize=9)
    for spine in ax.spines.values():
        spine.set_color("#1E293B")
        spine.set_linewidth(1.2)
    ax.grid(color="#1E293B", linestyle="--", linewidth=0.8, alpha=0.6)
    return fig, ax
