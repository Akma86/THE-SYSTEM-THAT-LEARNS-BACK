"""
Master CSS Design System for The Vanishing Currency.
"""

GLOBAL_THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Barlow+Condensed:wght@600;700;800;900&family=JetBrains+Mono:wght@400;500;700&family=Outfit:wght@400;600;700;800;900&display=swap');

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

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: #030712;
    color: #f8fafc;
    -webkit-font-smoothing: antialiased;
}

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

#MainMenu { visibility: hidden !important; }
footer { visibility: hidden !important; }
header { visibility: hidden !important; }

.block-container {
    max-width: 1240px;
    padding-top: 1.5rem !important;
    padding-bottom: 5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* Glassmorphism Containers */
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

/* Terminal Styling */
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

/* Inputs & Buttons */
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
.stat-value.orange { color: #fb923c; }
.stat-value.rose { color: #fb7185; }

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(24px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (max-width: 768px) {
    .main-title { font-size: 2.8rem; letter-spacing: -1px; }
    .glass-card { padding: 1.75rem 1.25rem; }
    .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
}
</style>
"""
