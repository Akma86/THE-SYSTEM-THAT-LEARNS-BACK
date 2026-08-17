"""
The System That Learns Back
Main Application Entrypoint
"""
import streamlit as st

from src.config import GAME_CONFIG
from src.components import GLOBAL_THEME_CSS
from src.stages import (
    intro_page,
    stage1_page,
    stage2_page,
    stage3_page,
    stage4_page,
    finish_page,
    ending_page,
    final_page,
)

# ==============================================================================
# STREAMLIT APP CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title=GAME_CONFIG["title"],
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject Master Global CSS
st.markdown(GLOBAL_THEME_CSS, unsafe_allow_html=True)

# Initialize Session State
if "current_stage" not in st.session_state:
    st.session_state.current_stage = 0

# ==============================================================================
# SIDEBAR / CYBER DECK NAVIGATOR
# ==============================================================================
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0;">
        <div style="font-family:'Space Mono', monospace; font-size:0.8rem; color:#38bdf8; letter-spacing:2px; margin-bottom:4px;">
            FINCORE::CONSOLE
        </div>
        <div style="font-family:'Outfit', sans-serif; font-size:1.4rem; font-weight:800; color:#f8fafc;">
            CYBER DECK
        </div>
    </div>
    """, unsafe_allow_html=True)

    stage_options = {
        0: "00 · Intro // Briefing",
        1: "01 · Stage 1: Noise",
        2: "02 · Stage 2: Convergence",
        3: "03 · Stage 3: Access",
        4: "04 · Stage 4: Extraction",
        5: "05 · Climax: Finish",
        6: "06 · The Truth: Ending",
        7: "07 · Archive: Final"
    }

    selected_stage = st.selectbox(
        "🎛️ Jump to Stage (Dev Mode):",
        options=list(stage_options.keys()),
        format_func=lambda x: stage_options[x],
        index=st.session_state.current_stage
    )

    if selected_stage != st.session_state.current_stage:
        st.session_state.current_stage = selected_stage
        st.rerun()

    st.markdown("---")
    if st.button("🔄 Reset Investigation to Start"):
        st.session_state.current_stage = 0
        st.rerun()

    st.markdown(f"""
    <div style="font-family:'Space Mono', monospace; font-size:0.75rem; color:#64748b; line-height:1.6; margin-top:2rem; text-align:center;">
        {GAME_CONFIG['organization']}<br>
        v{GAME_CONFIG['version']} · STABLE
    </div>
    """, unsafe_allow_html=True)


# ==============================================================================
# STAGE ROUTER
# ==============================================================================
stage_router = {
    0: intro_page,
    1: stage1_page,
    2: stage2_page,
    3: stage3_page,
    4: stage4_page,
    5: finish_page,
    6: ending_page,
    7: final_page,
}

current_stage = st.session_state.current_stage
stage_handler = stage_router.get(current_stage, intro_page)
stage_handler()