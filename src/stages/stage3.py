"""
Stage 3: Shadow Access // The Forgotten Step
"""
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from src.components import render_cyber_hud, render_stage_banner, apply_cyber_plot_style
from src.utils import load_stage3_data, validate_stage3_answer


def stage3_page():
    # 1. Cyber HUD
    render_cyber_hud(current_stage=3)

    # 2. Stage Banner
    ticker_items = [
        {"text": "ACCESS_LOG: ID_NULL", "hot": True},
        {"text": "DEPT: —", "hot": False},
        {"text": "PRIV: ROOT", "warn": True},
        {"text": "SINCE: DEPLOY_v1", "hot": False},
        {"text": "ARCHIVE ✓ · DB_TXN ✓ · CORE_SRV ✓", "hot": True},
        {"text": "BACKDOOR? NO.", "hot": False},
        {"text": "BUILT-IN FROM ORIGIN", "warn": True},
        {"text": "TIMESTAMP: [EPOCH]", "hot": False},
        {"text": "INTRUDER: NONE", "hot": True},
    ]
    render_stage_banner(
        stage_num="03",
        chapter_num="03",
        title_line1="The Forgotten",
        title_line2="Step",
        accent_color="#06b6d4",
        meta_tags=["id: null", "access: full", "present since v1", "not an intruder", "stage: access"],
        ticker_items=ticker_items,
        node_name="NODE_C",
        status_label="RESTRICTED // LVL-3",
    )

    # 3. Load Data
    df_access, df_system = load_stage3_data()

    # 4. Hero & Story
    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🧩 Stage 3</div>
        <div class="subtitle">Shadow Access // The Forgotten Step</div>
        <div class="story-text">
All forensic traces lead to the central data vault gateway.

Access logs are unsealed.
Initially, every single record appears standard and protocol-compliant.

However…
<b>an irreconcilable paradox surfaces in the authentication registry.</b>
<hr>
<i>"All users must enter through the login gateway..."</i>
<i>"...or at least, by mandatory policy they should."</i>
<hr>
When access activity per user is cross-referenced against official server login handshakes,
a chilling discrepancy arises:

An entity continuously reads tables, executes modifications, and manipulates files…
<b>without ever having logged into the system even once.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 5. Live Summary Stat Grid
    access_users = set(df_access['user_id'].dropna().unique())
    login_users = set(df_system[df_system['event'].str.contains('login', case=False, na=False)]['user_id'].dropna().unique())
    ghost_users = access_users - login_users

    st.markdown(f"""
    <div class="stat-grid">
        <div class="stat-box">
            <div class="stat-label">Total Access Events</div>
            <div class="stat-value cyan">{len(df_access)} Events</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">System Login Events</div>
            <div class="stat-value emerald">{len(df_system)} Logs</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Active User IDs</div>
            <div class="stat-value amber">{len(access_users)} Entities</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Unauthenticated Access</div>
            <div class="stat-value rose">{len(ghost_users)} Flagged</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 6. Data Log Section
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📂 Forensic Log Comparison: Access vs System</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📋 Access Log Forensics", "🛡️ System Security Events"])

    with tab1:
        st.markdown("<div style='font-size:0.9rem; color:#94a3b8; margin-bottom:0.75rem;'>Direct database manipulation and transaction ledger file reads:</div>", unsafe_allow_html=True)
        st.dataframe(df_access, use_container_width=True, height=280)

    with tab2:
        st.markdown("<div style='font-size:0.9rem; color:#94a3b8; margin-bottom:0.75rem;'>Official server session handshakes and authentication logs:</div>", unsafe_allow_html=True)
        st.dataframe(df_system, use_container_width=True, height=280)

    st.markdown('</div>', unsafe_allow_html=True)

    # 7. Visualization Section
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Hourly User Activity Distribution Matrix</div>', unsafe_allow_html=True)

    df_access["hour"] = df_access["timestamp"].dt.hour
    pivot = df_access.pivot_table(
        index="user_id",
        columns="hour",
        aggfunc="size",
        fill_value=0
    )

    fig, ax = plt.subplots(figsize=(13, 6), dpi=180)
    apply_cyber_plot_style(fig, ax, bg_color="#040914")

    sns.heatmap(
        pivot,
        cmap="icefire",
        ax=ax,
        linewidths=0.5,
        linecolor="#0B1120",
        cbar_kws={'label': 'Action Frequency (count)'}
    )

    ax.set_title("USER ACTIVITY TIMELINE // HOURLY ACTIVITY MATRIX", fontsize=11, color="#94A3B8", pad=12, fontfamily="monospace")
    ax.set_xlabel("Hour of Day (00:00 - 23:00)", fontsize=9, color="#94A3B8", fontfamily="monospace")
    ax.set_ylabel("User Identifier", fontsize=9, color="#94A3B8", fontfamily="monospace")
    ax.tick_params(colors="#94A3B8", labelsize=8.5)

    st.pyplot(fig)
    plt.close(fig)

    st.markdown("""
    <div class="terminal">
        <div class="terminal-header">
            <span class="term-dot red"></span>
            <span class="term-dot yellow"></span>
            <span class="term-dot green"></span>
            <span class="terminal-title">ACCESS PARADOX ANOMALY LOG</span>
        </div>
💡 <b>FORENSIC INVESTIGATION HINT:</b><br>
• Every legitimate human user records a `login_success` event in the `System Log` prior to issuing commands in the `Access Log`.<br>
• Detect the single User ID that is <b>consistently active across all 24 hours</b> in the Access Log, yet <b>lacks even a single login_success</b> in the System Log!<br>
• This entity is not an outsider or an intruder… it resides natively within the core architecture.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 8. Final Challenge Section
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Identify the Shadow Entity (Ghost User)</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="story-text" style="margin-bottom:1.5rem;">
Which User ID operates actively inside the system without ever undergoing the required login authentication process?
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input("Enter User ID:", placeholder="e.g. XJ-9A", key="stage3_answer")

    if st.button("🔍 Verify Entity Identity", key="stage3_btn"):
        if validate_stage3_answer(answer):
            st.success("✅ ANOMALY DETECTED // Shadow Entity 'XJ-9A' Confirmed!")
            st.markdown("""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="term-dot red"></span>
                    <span class="term-dot yellow"></span>
                    <span class="term-dot green"></span>
                    <span class="terminal-title">SYS_IDENTITY // RESOLVED</span>
                </div>
&gt; <i>"It never logged in..."</i><br>
&gt; <i>"...yet it pulses through every second of system runtime."</i><br><br>
&gt; That is no ordinary human operator.<br>
&gt; That is an internal architectural daemon embedded since the initial release.<br><br>
&gt; <i>Opening Stage 4 dossier: Extraction...</i>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.current_stage = 4
            st.rerun()
        else:
            st.error("❌ Incorrect User ID. Compare the active users in Access Log against those with verified login_success in System Log.")

    st.markdown('</div>', unsafe_allow_html=True)
