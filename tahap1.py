import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os
from ui_components import render_cyber_hud, render_stage_banner, apply_cyber_plot_style


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
        title_line1="Gemuruh",
        title_line2="Dalam Diam",
        accent_color="#10b981",
        meta_tags=["anomali terdeteksi", "audit: [null]", "signal: terlalu stabil", "stage: noise"],
        ticker_items=ticker_items,
        node_name="NODE_A",
        status_label="RESTRICTED // LVL-1",
    )

    # 3. Load Data
    data_path = "./data/stage1.csv"
    if not os.path.exists(data_path):
        data_path = "data/stage1.csv"
    df = pd.read_csv(data_path)

    # 4. Hero & Story
    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🧩 Stage 1</div>
        <div class="subtitle">Noise // Gemuruh Dalam Diam</div>
        <div class="story-text">
Malam itu, sistem keuangan nasional berjalan seperti biasa.

Tidak ada gangguan.
Tidak ada alarm.
Tidak ada alasan untuk khawatir.

Setidaknya… di permukaan.
<hr>
Transaksi mengalir seperti setiap hari.
Angka naik dan turun sesuai pola yang bisa diprediksi.

Semuanya terlihat stabil.
<b>Terlalu stabil.</b>
<hr>
Seorang analis membuka dashboard utama.
Ia berhenti.

Bukan karena ada error.
Tapi karena… <b>sesuatu terlihat terlalu "rapi".</b>
<hr>
Dalam lautan data yang bergerak acak,
ada satu bagian yang tidak ikut bergerak.

Tidak mencolok. Tidak mencurigakan.
Hanya… <b>berbeda.</b>
<hr>
Dan di sistem yang seharusnya tidak punya ingatan,
bagian itu terasa seperti sesuatu yang sedang menunggu untuk dikenali.
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
    st.markdown('<div class="section-title">🔍 Modul Analisis Forensik Data</div>', unsafe_allow_html=True)

    option = st.radio(
        "Pilih Instrumen Analisis:",
        ["🔥 Heatmap Korelasi Antar-Akun", "📋 Tabel Data Transaksi Lengkap"],
        horizontal=True
    )

    if "Heatmap" in option:
        st.markdown("""
        <div class="story-text" style="margin-bottom:1.5rem;">
Tidak semua yang berbeda itu mencolok.
Kadang… justru yang paling <b>"tenang"</b> dan memiliki korelasi tersembunyi.
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
Kadang jawabannya tidak muncul dari perbandingan satu per satu…
melainkan dari <b>melihat seluruh matriks data sekaligus.</b>
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(df, use_container_width=True, height=350)
        st.info("💡 **HINT ANALISIS**: Perhatikan pergerakan nilai data. Tidak semua anomali terlihat seperti spike atau error yang meledak — beberapa anomali justru bersembunyi dalam pola yang terlalu teratur.")

    st.markdown('</div>', unsafe_allow_html=True)

    # 8. Final Clue & Hidden Message Section
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Dekripsi Pesan Tersembunyi</div>', unsafe_allow_html=True)

    ascii_path = "assets/ascii.png"
    if os.path.exists(ascii_path):
        img = Image.open(ascii_path)
        st.image(img, use_container_width=True, caption="[RESTRICTED ARTIFACT] // Memori ASCII Buffer Dump")

    st.markdown("""
    <div class="story-text" style="margin-top:1.5rem; margin-bottom:1.5rem;">
Sebuah pesan terenkripsi terpatri dalam fragmen ASCII buffer dump di atas.
Baca dan temukan frasa tersembunyi untuk membuka akses ke Stage berikutnya:
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input(
        "Masukkan kata/frasa yang kamu temukan:",
        placeholder="Ketik jawaban di sini (contoh: YOU ARE LATE)...",
        key="stage1_input"
    )

    if st.button("🔓 Kirim & Validasi Akses", key="stage1_btn"):
        cleaned = answer.strip().upper().replace("'", "").replace(".", "")
        valid_answers = ["YOU ARE LATE", "YOU WERE LATE", "YOURE LATE", "YOU WERE LATE"]

        if cleaned in valid_answers:
            st.success("✅ ACCESS GRANTED // Kunci Otentikasi Terbuka!")
            st.markdown("""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="term-dot red"></span>
                    <span class="term-dot yellow"></span>
                    <span class="term-dot green"></span>
                    <span class="terminal-title">SYS_DECRYPT // SUCCESS</span>
                </div>
&gt; Layar berkedip.<br>
&gt; Satu baris teks muncul: <b>YOU ARE LATE.</b><br><br>
&gt; Tidak ada konteks.<br>
&gt; Tidak ada sumber.<br><br>
&gt; Dan untuk pertama kalinya— sistem tidak mencoba menjelaskan apa pun.<br>
&gt; <i>Mengalihkan protokol investigasi ke Stage 2: Convergence...</i>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.current_stage = 2
            st.rerun()
        else:
            st.error("❌ Jawaban belum tepat. Perhatikan pola teks pada gambar ASCII buffer dump dengan teliti.")
            st.warning("⚠️ Protokol sistem: Gagal memvalidasi token. Coba telusuri kembali huruf per huruf.")

    st.markdown('</div>', unsafe_allow_html=True)