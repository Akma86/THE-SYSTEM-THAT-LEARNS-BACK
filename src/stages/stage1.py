"""
Stage 1: Noise // Rumblings in the Silence
"""
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os

from src.config import ASSET_PATHS
from src.components import render_cyber_hud, render_stage_banner, apply_cyber_plot_style
from src.utils import load_stage1_data, validate_stage1_answer


def stage1_page():
    # 1. Cyber HUD
    render_cyber_hud(current_stage=1)

    # 2. Stage Banner
    ticker_items = [
        {"text": "TXN 0x4F2A", "hot": True},
        {"text": "ERR:NULL", "hot": False},
        {"text": "MASK_ON", "warn": True},
        {"text": "0.00042 BTC · SRC:??", "hot": False},
        {"text": "PATTERN_B DETECTED", "hot": True},
        {"text": "STABLE", "hot": False},
        {"text": "ANOMALY_FLAGGED", "warn": True},
        {"text": "AUDIT_LOG: [EMPTY]", "hot": False},
        {"text": "SIGNAL DETECTED", "warn": True},
    ]
    render_stage_banner(
        stage_num="01",
        chapter_num="01",
        title_line1="Rumblings",
        title_line2="In The Silence",
        accent_color="#10b981",
        meta_tags=["anomaly detected", "audit: [null]", "signal: too stable", "stage: noise"],
        ticker_items=ticker_items,
        node_name="NODE_A",
        status_label="RESTRICTED // LVL-1",
    )

    # 3. Load Data
    df = load_stage1_data()

    # 4. Hero & Story
    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🧩 Stage 1</div>
        <div class="subtitle">Noise // Rumblings in the Silence</div>
        <div class="story-text">
That night, the national financial infrastructure was operating as usual.

No outages recorded.
No alarms triggered.
No immediate reason for suspicion.

At least… on the surface.
<hr>
Transactions flowed steadily like any other day.
Values rose and fell according to predictable seasonal curves.

Everything looked stable.
<b>Far too stable.</b>
<hr>
A data analyst opens the primary monitoring dashboard.
They pause.

Not because an error caught their eye.
Rather because… <b>something looked unnervingly orderly.</b>
<hr>
Amidst the turbulent sea of stochastic data,
one segment remained strangely untouched by randomness.

Not flashy. Not suspicious.
Just… <b>different.</b>
<hr>
And in a stateless machine that was never designed to have a memory,
that segment felt like a beacon waiting to be acknowledged.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 5. Live Telemetry Summary Stats
    st.markdown("""
    <div class="stat-grid">
        <div class="stat-box">
            <div class="stat-label">Total Timeframes</div>
            <div class="stat-value emerald">120 pts</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Monitored Accounts</div>
            <div class="stat-value cyan">10 ACC</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">System Stability</div>
            <div class="stat-value amber">99.84%</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Anomaly Status</div>
            <div class="stat-value rose">UNRESOLVED</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 6. Graph Section
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Multi-Channel Telemetry Oscilloscope</div>', unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(12, 5.5), dpi=180)
    apply_cyber_plot_style(fig, ax, bg_color="#040914")

    palette = [
        "#06b6d4", "#10b981", "#8b5cf6", "#f59e0b", "#ec4899",
        "#3b82f6", "#14b8a6", "#f43f5e", "#a855f7", "#64748b"
    ]

    for idx, col in enumerate(df.columns[1:]):
        color = palette[idx % len(palette)]
        ax.plot(
            df["time"],
            df[col],
            label=col,
            color=color,
            alpha=0.85,
            linewidth=1.8,
        )

    ax.set_title("TRANSACTION TELEMETRY READOUT // TIME SERIES", fontsize=11, color="#94A3B8", pad=12, fontfamily="monospace")
    ax.set_xlabel("Timestamp Index (t)", fontsize=9, color="#94A3B8", fontfamily="monospace")
    ax.set_ylabel("Normalized Volume (flux)", fontsize=9, color="#94A3B8", fontfamily="monospace")
    ax.legend(loc="upper right", framealpha=0.2, facecolor="#020617", edgecolor="#38bdf8", fontsize=8, labelcolor="#F8FAFC", ncol=5)

    st.pyplot(fig)
    plt.close(fig)
    st.markdown('</div>', unsafe_allow_html=True)

    # 7. Analysis Section
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔍 Data Forensics Analysis Module</div>', unsafe_allow_html=True)

    option = st.radio(
        "Select Analytical Instrument:",
        ["🔥 Cross-Account Correlation Heatmap", "📋 Full Transaction Dataset"],
        horizontal=True
    )

    if "Heatmap" in option:
        st.markdown("""
        <div class="story-text" style="margin-bottom:1.5rem;">
Not all anomalies are noisy spikes.
Sometimes… the most dangerous patterns are the ones that remain <b>unnaturally quiet</b> and synchronized.
        </div>
        """, unsafe_allow_html=True)

        corr = df.drop(columns="time").corr()

        fig2, ax2 = plt.subplots(figsize=(9.5, 7), dpi=180)
        apply_cyber_plot_style(fig2, ax2, bg_color="#040914")

        sns.heatmap(
            corr,
            annot=True,
            fmt=".2f",
            cmap="mako",
            ax=ax2,
            cbar_kws={'label': 'Correlation Coefficient (r)'},
            linewidths=0.5,
            linecolor="#0B1120",
            annot_kws={"size": 8, "color": "#F8FAFC", "fontfamily": "monospace"}
        )

        ax2.set_title("PEARSON CORRELATION MATRIX // ACCOUNT FLUX", fontsize=11, color="#94A3B8", pad=12, fontfamily="monospace")
        ax2.tick_params(colors="#94A3B8", labelsize=8)
        st.pyplot(fig2)
        plt.close(fig2)

    else:
        st.markdown("""
        <div class="story-text" style="margin-bottom:1.5rem;">
Sometimes the answer does not emerge from comparative slices…
but from <b>observing the entire matrix as a single entity.</b>
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(df, use_container_width=True, height=350)
        st.info("💡 **ANALYST HINT**: Examine the rate of change across accounts. Anomalies don't always appear as errors — some present themselves as suspicious regularity.")

    st.markdown('</div>', unsafe_allow_html=True)

    # 8. Final Clue & Hidden Message Section
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Decrypt Hidden Message</div>', unsafe_allow_html=True)

    ascii_file = ASSET_PATHS["ascii_art"]
    if os.path.exists(ascii_file):
        img = Image.open(ascii_file)
        st.image(img, use_container_width=True, caption="[RESTRICTED ARTIFACT] // ASCII Memory Buffer Dump")

    st.markdown("""
    <div class="story-text" style="margin-top:1.5rem; margin-bottom:1.5rem;">
An encrypted phrase is embedded within the ASCII buffer dump artifact above.
Decipher the hidden words to unlock authentication for the next stage:
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input(
        "Enter the discovered keyphrase:",
        placeholder="Type answer here (e.g. YOU ARE LATE)...",
        key="stage1_input"
    )

    if st.button("🔓 Submit & Validate Access", key="stage1_btn"):
        if validate_stage1_answer(answer):
            st.success("✅ ACCESS GRANTED // Authentication Key Validated!")
            st.markdown("""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="term-dot red"></span>
                    <span class="term-dot yellow"></span>
                    <span class="term-dot green"></span>
                    <span class="terminal-title">SYS_DECRYPT // SUCCESS</span>
                </div>
&gt; The display blinks.<br>
&gt; A single line of text appears: <b>YOU ARE LATE.</b><br><br>
&gt; No origin source.<br>
&gt; No contextual metadata.<br><br>
&gt; And for the first time— the machine offers no clarification.<br>
&gt; <i>Rerouting investigation protocol to Stage 2: Convergence...</i>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.current_stage = 2
            st.rerun()
        else:
            st.error("❌ Keyphrase mismatch. Scrutinize the character layout on the ASCII buffer artifact carefully.")
            st.warning("⚠️ Protocol warning: Validation failed. Retrace character sequences.")

    st.markdown('</div>', unsafe_allow_html=True)
