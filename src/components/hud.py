"""
Cyber HUD Navigation component for The Vanishing Currency.
"""
import streamlit as st


def render_cyber_hud(current_stage: int):
    """Renders the persistent cyber investigation HUD across stages."""
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
    <style>
    .cyber-hud {{
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
    }}
    .hud-left {{
        display: flex;
        align-items: center;
        gap: 14px;
    }}
    .hud-badge-logo {{
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
    }}
    .hud-status-dot {{
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #10b981;
        box-shadow: 0 0 10px #10b981, 0 0 20px #10b981;
        animation: hudPulse 2s infinite ease-in-out;
    }}
    @keyframes hudPulse {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(1.3); }}
    }}
    .hud-clearance {{
        font-family: 'Space Mono', monospace;
        font-size: 0.75rem;
        letter-spacing: 1.5px;
        color: #e2e8f0;
        text-transform: uppercase;
    }}
    .hud-clearance span {{
        color: #f43f5e;
        font-weight: 700;
    }}
    .hud-stages-track {{
        display: flex;
        align-items: center;
        gap: 6px;
        background: rgba(2, 6, 23, 0.7);
        padding: 6px 12px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }}
    .stage-pill {{
        font-family: 'Space Mono', monospace;
        font-size: 0.72rem;
        letter-spacing: 1px;
        padding: 4px 10px;
        border-radius: 8px;
        color: #64748b;
        border: 1px solid transparent;
        transition: all 0.3s ease;
    }}
    .stage-pill.active {{
        background: linear-gradient(135deg, rgba(37, 99, 235, 0.35), rgba(124, 58, 237, 0.35));
        border-color: rgba(56, 189, 248, 0.5);
        color: #38bdf8;
        font-weight: 700;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.25);
    }}
    .stage-pill.done {{
        background: rgba(16, 185, 129, 0.12);
        border-color: rgba(16, 185, 129, 0.3);
        color: #10b981;
    }}
    @media (max-width: 768px) {{
        .cyber-hud {{ flex-direction: column; align-items: flex-start; }}
    }}
    </style>

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
