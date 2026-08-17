import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from ui_components import render_cyber_hud, render_stage_banner, apply_cyber_plot_style


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
        title_line1="Langkah Yang",
        title_line2="Terlupakan",
        accent_color="#06b6d4",
        meta_tags=["id: null", "akses: penuh", "ada sejak awal", "bukan penyusup", "stage: access"],
        ticker_items=ticker_items,
        node_name="NODE_C",
        status_label="RESTRICTED // LVL-3",
    )

    # 3. Load Data
    access_path = "./data/stage3_access.csv" if os.path.exists("./data/stage3_access.csv") else "data/stage3_access.csv"
    system_path = "./data/stage3_system.csv" if os.path.exists("./data/stage3_system.csv") else "data/stage3_system.csv"

    df_access = pd.read_csv(access_path)
    df_system = pd.read_csv(system_path)

    df_access["timestamp"] = pd.to_datetime(df_access["timestamp"])
    df_system["timestamp"] = pd.to_datetime(df_system["timestamp"])

    # 4. Hero & Story
    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🧩 Stage 3</div>
        <div class="subtitle">Shadow Access // Langkah Yang Terlupakan</div>
        <div class="story-text">
Semua jejak mengarah ke satu pintu masuk pusat data.

Log akses dibuka.
Awalnya seluruh entri terlihat normal dan sesuai protokol.

Namun…
<b>ada sesuatu yang tidak masuk akal dalam catatan autentikasi.</b>
<hr>
<i>"Semua user masuk lewat pintu login..."</i>
<i>"...atau setidaknya, secara regulasi seharusnya begitu."</i>
<hr>
Ketika pergerakan aktivitas setiap akun dicocokkan dengan catatan otentikasi sistem,
muncul paradoks yang membingungkan:

Ada entitas yang terus-menerus memanipulasi file, mengekstraksi tabel, dan mengubah parameter…
<b>namun tidak pernah tercatat melewati gerbang login satu kali pun.</b>
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
    st.markdown('<div class="section-title">📂 Komparasi Log Forensik: Akses vs Sistem</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📋 Access Log Forensics", "🛡️ System Security Events"])

    with tab1:
        st.markdown("<div style='font-size:0.9rem; color:#94a3b8; margin-bottom:0.75rem;'>Catatan interaksi langsung pada basis data dan file transaksi:</div>", unsafe_allow_html=True)
        st.dataframe(df_access, use_container_width=True, height=280)

    with tab2:
        st.markdown("<div style='font-size:0.9rem; color:#94a3b8; margin-bottom:0.75rem;'>Catatan otentikasi resmi dan session handshake dari server gateway:</div>", unsafe_allow_html=True)
        st.dataframe(df_system, use_container_width=True, height=280)

    st.markdown('</div>', unsafe_allow_html=True)

    # 7. Visualization Section
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📊 Matriks Distribusi Aktivitas Jam per User</div>', unsafe_allow_html=True)

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
💡 <b>HINT INVESTIGASI FORENSIK:</b><br>
• Setiap user resmi tercatat melakukan `login_success` di `System Log` sebelum mengeksekusi perintah di `Access Log`.<br>
• Periksa apakah ada satu User ID yang <b>aktif secara konstan setiap jam</b> di Access Log, namun <b>sama sekali tidak pernah memiliki riwayat login_success</b> di System Log!<br>
• Entitas ini bukan tamu, bukan penyusup luar… entitas ini hidup di dalam arsitektur dasar.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 8. Final Challenge Section
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Identifikasi Entitas Bayangan (Shadow User)</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="story-text" style="margin-bottom:1.5rem;">
Siapakah User ID anomali yang selalu aktif beroperasi di dalam sistem tanpa pernah sekalipun melakukan proses login resmi?
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input("Masukkan User ID:", placeholder="Contoh: XJ-9A", key="stage3_answer")

    if st.button("🔍 Verifikasi Identitas Entitas", key="stage3_btn"):
        cleaned_ans = answer.strip().upper().replace(" ", "").replace("_", "-")

        if cleaned_ans in ["XJ-9A", "XJ9A"]:
            st.success("✅ ANOMALY DETECTED // Entitas 'XJ-9A' Terkonfirmasi!")
            st.markdown("""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="term-dot red"></span>
                    <span class="term-dot yellow"></span>
                    <span class="term-dot green"></span>
                    <span class="terminal-title">SYS_IDENTITY // RESOLVED</span>
                </div>
&gt; <i>"Dia tidak pernah login..."</i><br>
&gt; <i>"...tapi selalu ada di setiap detak jam sistem."</i><br><br>
&gt; Itu bukan user manusia biasa.<br>
&gt; Itu adalah proses internal yang tersembunyi sejak versi pertama sistem dirilis.<br><br>
&gt; <i>Membuka protokol investigasi Stage 4: Extraction...</i>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.current_stage = 4
            st.rerun()
        else:
            st.error("❌ User ID salah. Bandingkan daftar user di Access Log dengan daftar akun yang berhasil login di System Log.")

    st.markdown('</div>', unsafe_allow_html=True)