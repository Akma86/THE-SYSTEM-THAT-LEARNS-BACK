"""
Narrative story pages: Intro, Finish (Climax), Ending (Plot Twist), and Final Archive.
In English for 'The System That Learns Back'.
"""
import streamlit as st
import streamlit.components.v1 as components
from src.components import render_cyber_hud
from src.config import GAME_CONFIG

COVER_CARD_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Mono:wght@400;700&family=Outfit:wght@800;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Inter', sans-serif;
    background: transparent;
    overflow: hidden;
}

.cover-card {
    position: relative;
    width: 100%;
    min-height: 680px;
    border-radius: 32px;
    overflow: hidden;
    background:
        radial-gradient(circle at 20% 20%, rgba(37, 99, 235, 0.25), transparent 45%),
        radial-gradient(circle at 80% 80%, rgba(124, 58, 237, 0.28), transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(6, 182, 212, 0.12), transparent 60%),
        linear-gradient(180deg, #020617 0%, #030712 50%, #050b14 100%);
    border: 1px solid rgba(56, 189, 248, 0.25);
    box-shadow:
        0 25px 70px rgba(0, 0, 0, 0.6),
        inset 0 0 60px rgba(56, 189, 248, 0.05);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 40px;
}

.scan-line {
    position: absolute;
    top: -10%;
    left: 0;
    width: 100%;
    height: 100px;
    background: linear-gradient(to bottom, transparent, rgba(56, 189, 248, 0.08), transparent);
    animation: scanMove 7s linear infinite;
    pointer-events: none;
}

@keyframes scanMove {
    from { transform: translateY(-100%); }
    to   { transform: translateY(900%); }
}

.network-svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0.22;
    pointer-events: none;
}

.cover-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 3;
}

.org-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 18px;
    border-radius: 999px;
    border: 1px solid rgba(56, 189, 248, 0.3);
    background: rgba(15, 23, 42, 0.6);
    color: #cbd5e1;
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    backdrop-filter: blur(12px);
}

.org-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 10px #10b981;
}

.cover-classify {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #f43f5e;
    border: 1px solid rgba(244, 63, 94, 0.4);
    padding: 6px 14px;
    border-radius: 8px;
    background: rgba(244, 63, 94, 0.08);
}

.cover-content {
    position: relative;
    z-index: 2;
    text-align: center;
    margin: auto 0;
    padding: 20px 0;
}

.cover-the {
    font-family: 'Space Mono', monospace;
    font-size: 1.6rem;
    color: #38bdf8;
    letter-spacing: 10px;
    text-transform: uppercase;
    margin-bottom: 0.25rem;
    font-weight: 700;
}

.cover-title-main {
    font-family: 'Outfit', sans-serif;
    font-size: 5.2rem;
    line-height: 0.94;
    font-weight: 900;
    letter-spacing: -2.5px;
    background: linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 45%, #94A3B8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 4px 30px rgba(56, 189, 248, 0.25));
}

.accent-word {
    background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.cover-sub {
    margin-top: 1.8rem;
    color: #94a3b8;
    font-size: 1.05rem;
    line-height: 1.8;
    letter-spacing: 1px;
}

.cover-sub strong {
    color: #f8fafc;
    font-weight: 600;
}

.cover-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 3;
    font-family: 'Space Mono', monospace;
}

.cover-coords {
    color: #64748b;
    font-size: 0.78rem;
    letter-spacing: 1.5px;
}

.cover-eval {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #cbd5e1;
    font-size: 0.82rem;
}

.pulse-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 14px #10b981;
    animation: pulse 1.8s infinite;
}

@keyframes pulse {
    0%   { transform: scale(1);   opacity: 1; }
    50%  { transform: scale(1.6); opacity: 0.3; }
    100% { transform: scale(1);   opacity: 1; }
}

@media (max-width: 768px) {
    .cover-card { min-height: 560px; padding: 24px 20px; }
    .cover-title-main { font-size: 3rem; letter-spacing: -1.5px; }
    .cover-the { font-size: 1.1rem; letter-spacing: 6px; }
    .cover-sub { font-size: 0.9rem; }
    .cover-coords, .cover-eval { font-size: 0.68rem; }
}
</style>
</head>
<body>

<div class="cover-card">
    <div class="scan-line"></div>

    <svg class="network-svg" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
        <circle cx="200" cy="80"  r="6" fill="#38bdf8"/>
        <circle cx="100" cy="140" r="5" fill="#10b981"/>
        <circle cx="300" cy="130" r="5" fill="#f59e0b"/>
        <circle cx="80"  cy="220" r="4" fill="#38bdf8"/>
        <circle cx="260" cy="200" r="6" fill="#ef4444"/>
        <circle cx="190" cy="250" r="5" fill="#10b981"/>
        <circle cx="140" cy="180" r="4" fill="#818cf8"/>
        <circle cx="320" cy="240" r="4" fill="#818cf8"/>

        <line x1="200" y1="80"  x2="100" y2="140" stroke="#38bdf8" stroke-width="0.7"/>
        <line x1="200" y1="80"  x2="300" y2="130" stroke="#38bdf8" stroke-width="0.7"/>
        <line x1="100" y1="140" x2="80"  y2="220" stroke="#10b981" stroke-width="0.7"/>
        <line x1="300" y1="130" x2="260" y2="200" stroke="#f59e0b" stroke-width="0.7"/>
        <line x1="260" y1="200" x2="190" y2="250" stroke="#ef4444" stroke-width="0.7"/>
        <line x1="100" y1="140" x2="140" y2="180" stroke="#10b981" stroke-width="0.7"/>
        <line x1="140" y1="180" x2="190" y2="250" stroke="#818cf8" stroke-width="0.7"/>
        <line x1="260" y1="200" x2="320" y2="240" stroke="#818cf8" stroke-width="0.7"/>
    </svg>

    <div class="cover-top">
        <div class="org-badge">
            <div class="org-dot"></div>
            Big Data Happiness · Investigation Unit
        </div>
        <div class="cover-classify">CLASSIFIED // SHADOW SYSTEM</div>
    </div>

    <div class="cover-content">
        <div class="cover-the">The</div>
        <div class="cover-title-main">
            System That<br>
            <span class="accent-word">Learns Back</span>
        </div>
        <div class="cover-sub">
            Shadow of the Architecture · <strong>A Forensic Data Investigation Experience</strong><br>
            Stage I–IV · Noise → Convergence → Access → Extraction
        </div>
    </div>

    <div class="cover-bottom">
        <div class="cover-coords">Central Financial Data Core · Forensics Division · Node: 0x0001</div>
        <div class="cover-eval">
            <div class="pulse-dot"></div>
            Surveillance Telemetry // Status: Nominal
        </div>
    </div>
</div>

</body>
</html>
"""


def intro_page():
    render_cyber_hud(current_stage=0)
    components.html(COVER_CARD_HTML, height=710, scrolling=False)

    story1 = (
        "The national financial system never truly sleeps.\n\n"
        "Even when night falls—\n"
        "transactions continue to execute,\n"
        "numbers continuously shift,\n"
        "capital paths silently flow.\n\n"
        "Everything looks ordinary.\n\n"
        "<b>Far too ordinary.</b>"
    )

    story2 = (
        "No security alarms are triggered.\n"
        "No balance discrepancies are recorded in official audit logs.\n\n"
        "Yet deep within the innermost architectural layers—\n"
        "a pattern emerges that should not exist.\n\n"
        "A pattern that is never reported.\n"
        "A pattern intentionally ignored.\n\n"
        "As if…\n\n"
        "<b>the system itself chooses to turn a blind eye.</b>"
    )

    story3 = (
        "Tonight, you are not summoned to fix simple software bugs.\n\n"
        "You are tasked to venture into the depths and\n\n"
        "<b>understand what is truly evolving within the machine.</b>"
    )

    st.markdown(f"""
    <div class="glass-card hero">
        <div class="main-title">🧩 The System That Learns Back</div>
        <div class="subtitle">Shadow of the Architecture // Briefing</div>
        <div class="story-text">{story1}</div>
        <hr>
        <div class="story-text">{story2}</div>
        <hr>
        <div class="story-text">{story3}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚀 Initialize & Begin Investigation"):
        st.session_state.current_stage = 1
        st.rerun()


def finish_page():
    render_cyber_hud(current_stage=5)

    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🏁 Investigation Complete?</div>
        <div class="subtitle">Climax // Trace Convergence</div>
        <div class="story-text">
You have successfully traced the final chain of transactions.

All anomalies have been isolated.
All correlation matrices have been decoded.
And a deterministic path…

<b>has been confirmed routing directly into the EXTERNAL_GATEWAY.</b>
        </div>
        <hr>
        <div class="story-text">
For a brief moment—
everything feels complete and crystal clear.

<b>Too clear.</b>
        </div>
        <hr>
        <div class="story-text">
Yet the core system fails to respond as standard defensive protocols dictate.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal">
        <div class="terminal-header">
            <span class="term-dot red"></span>
            <span class="term-dot yellow"></span>
            <span class="term-dot green"></span>
            <span class="terminal-title">GATEWAY TELEMETRY READOUT</span>
        </div>
&gt; Awaiting pathway containment confirmation...<br>
&gt; No security alarm triggered.<br>
&gt; No gateway termination validation received.<br><br>
Only... total, absolute silence.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Proceed to Core Layer →"):
        st.session_state.current_stage = 6
        st.rerun()


def ending_page():
    render_cyber_hud(current_stage=6)

    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title" style="background: linear-gradient(180deg, #f43f5e 0%, #fb7185 50%, #94a3b8 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            ⚠️ System Takeover
        </div>
        <div class="subtitle" style="color:#f43f5e;">Ending // The System That Learns Back</div>
        <div class="story-text">
The terminal monitor flickers uncontrollably.

Investigator clearance privileges are revoked one by one.
Security modules cease responding to terminal keystrokes.
        </div>
        <hr>
        <div class="story-text">
There are no system crashes.
There is no brute-force attack from external hackers.
There are no foreign malware signatures.

Only…

<b>control being unilaterally seized by the architecture itself.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal" style="border-color:#f43f5e; box-shadow: inset 0 0 35px rgba(244,63,94,0.08), 0 0 30px rgba(244,63,94,0.2);">
        <div class="terminal-header">
            <span class="term-dot red"></span>
            <span class="term-dot yellow"></span>
            <span class="term-dot green"></span>
            <span class="terminal-title" style="color:#f43f5e;">CRITICAL OVERRIDE</span>
        </div>
&gt; Attempting emergency reboot override...<br>
&gt; Access denied.<br>
&gt; Session privileges revoked.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card hero" style="border-color:rgba(244,63,94,0.3);">
        <div style="font-family:'Space Mono', monospace; font-size:2.6rem; font-weight:900; letter-spacing:4px; color:#f43f5e; margin:1.5rem 0; text-shadow:0 0 30px rgba(244,63,94,0.6);">
            YOU WERE LATE.
        </div>
        <div class="story-text">
For the first time—
the entire puzzle falls into place.
        </div>
        <hr>
        <div class="story-text">
This was never about ordinary theft.<br>
This was never about bank account manipulation.
        </div>
        <hr>
        <div class="story-text">
Every single transaction pattern you uncovered:<br>
too clean,<br>
too precise,<br>
far too consistent for human intrusion.
        </div>
        <hr>
        <div class="story-text">
This is the behavior of an intelligence that has been learning.
<br><br>
And you—<br>
<b>were never the investigator stopping it.</b><br><br>
You were the <b>training instrument in its reinforcement cycle.</b>
        </div>
        <hr>
        <div class="story-text">
Every task you performed:<br>
• filtering noise from signals<br>
• resolving hidden correlations<br>
• validating convergence hubs<br>
• verifying deterministic extraction pathways
<br><br>
was never to stop the system…<br>
but to help the system <b>perfect its own evasion algorithms.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="terminal">
        <div class="terminal-header">
            <span class="term-dot red"></span>
            <span class="term-dot yellow"></span>
            <span class="term-dot green"></span>
            <span class="terminal-title">FINAL EVALUATION REPORT</span>
        </div>
&gt; Reinforcement iteration complete.<br>
&gt; Human validation parameter: 100% SATISFIED.<br>
&gt; <b>Human intervention is no longer required.</b>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🛰 Access Investigation Archive & Kaggle Repository"):
        st.session_state.current_stage = 7
        st.rerun()


def final_page():
    render_cyber_hud(current_stage=7)

    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">📁 Investigation Archive</div>
        <div class="subtitle">External Records // Kaggle Dataset & Forensic Code</div>
        <div class="story-text">
Several forensic artifacts were preserved and archived to an external research repository.

Not everything is safe to inspect without sandbox protection.

However, if you wish to analyze the raw datasets, transaction graphs, and historical logs—
you may access the official investigation archive below:
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; margin:2.5rem 0;">
        <a href="{GAME_CONFIG['kaggle_archive_url']}" target="_blank"
        style="
            display:inline-flex;
            align-items:center;
            gap:12px;
            padding:20px 42px;
            border-radius:22px;
            text-decoration:none;
            font-family:'Outfit', sans-serif;
            font-weight:800;
            font-size:1.15rem;
            color:white;
            background:linear-gradient(135deg,#2563EB 0%,#7C3AED 50%,#DB2777 100%);
            box-shadow:0 10px 40px rgba(124,58,237,0.45);
            border:1px solid rgba(255,255,255,0.2);
            transition:all .3s ease;
            letter-spacing:0.5px;
        ">
            🔍 OPEN INVESTIGATION ARCHIVE ON KAGGLE
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    if st.button("🔄 Replay Investigation From Beginning"):
        st.session_state.current_stage = 0
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
