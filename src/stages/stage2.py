"""
Stage 2: Convergence // Bayangan Di Langit
"""
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

from src.components import render_cyber_hud, render_stage_banner, apply_cyber_plot_style
from src.utils import load_stage2_data, validate_stage2_answer


def stage2_page():
    # 1. Cyber HUD
    render_cyber_hud(current_stage=2)

    # 2. Stage Banner
    ticker_items = [
        {"text": "NODE_MERGE ████→█", "hot": True},
        {"text": "CONVERGENCE: 99.7%", "hot": False},
        {"text": "SHADOW_SYSTEM ACTIVE", "warn": True},
        {"text": "SIM:CROSS-BORDER", "hot": False},
        {"text": "ALL PATHS → ONE NODE", "hot": True},
        {"text": "TXN_LOOP ∞", "hot": False},
        {"text": "UNREGISTERED", "warn": True},
        {"text": "ENDPOINT: 0x0001", "hot": True},
    ]
    render_stage_banner(
        stage_num="02",
        chapter_num="02",
        title_line1="Bayangan",
        title_line2="Di Langit",
        accent_color="#f59e0b",
        meta_tags=["semua jalur → satu titik", "sistem bayangan", "lintas yurisdiksi", "tidak tercatat"],
        ticker_items=ticker_items,
        node_name="NODE_B",
        status_label="RESTRICTED // LVL-2",
    )

    # 3. Load Data
    df = load_stage2_data()

    # 4. Hero & Story
    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🧩 Stage 2</div>
        <div class="subtitle">Convergence // Bayangan Di Langit</div>
        <div class="story-text">
Awalnya tidak ada yang aneh.

Transaksi internasional berjalan seperti biasa.
Tidak ada pola yang mencurigakan.
Tidak ada pusat yang terlihat secara kasat mata.
<hr>
Namun ketika data divisualisasikan ulang ke dalam topologi jaringan…
<b>struktur mulai berubah.</b>
<hr>
Bukan karena datanya yang berubah.
Tapi karena <b>sudut pandang dalam memetakannya yang berbeda.</b>
<hr>
Beberapa node terlihat jauh lebih "berat" daripada yang lain.
Bukan secara volume nominal semata…
melainkan secara <b>sentralitas koneksi global.</b>
<hr>
Dan semakin lama diamati, semakin jelas satu kenyataan:
Sistem ini tidak tersebar secara acak.
Sistem ini <b>tertarik kuat menuju satu titik gravitasi.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 5. Live Summary Stat Grid
    st.markdown(f"""
    <div class="stat-grid">
        <div class="stat-box">
            <div class="stat-label">Total Transactions</div>
            <div class="stat-value amber">{len(df)} TXNs</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Source Countries</div>
            <div class="stat-value cyan">{df['source_country'].nunique()} Nodes</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Dest Countries</div>
            <div class="stat-value emerald">{df['destination_country'].nunique()} Nodes</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Network Topology</div>
            <div class="stat-value rose">DIRECTED GRAPH</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 6. Data Exploration Section
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📂 Matriks Transaksi Cross-Border Global</div>', unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True, height=280)
    st.markdown('</div>', unsafe_allow_html=True)

    # 7. Code Reconstruction & Network Visualization Section
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔍 Rekonstruksi Script Visualisasi Graph</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="story-text" style="margin-bottom:1.5rem;">
Seorang analis forensik sebelumnya mencoba memetakan topologi transaksi ini, namun scriptnya terputus pada deklarasi edge list.
Lengkapi parameter kolom sumber dan tujuan berikut agar mesin grafis dapat mengompilasi peta jaringan:
    </div>
    """, unsafe_allow_html=True)

    st.code("""
import networkx as nx
import matplotlib.pyplot as plt

# Bangun struktur edge list berdasarkan kolom DataFrame
G = nx.from_pandas_edgelist(df, source='...[A]...', target='...[B]...')

pos = nx.spring_layout(G, seed=42)
degree = dict(G.degree())
node_sizes = [degree[n] * 70 for n in G.nodes()]

nx.draw(G, pos, with_labels=True, node_size=node_sizes)
plt.show()
""", language="python")

    st.markdown('<div class="section-title" style="font-size:1.3rem; margin-top:1.5rem;">💻 Parameter Injeksi Kolom</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        A = st.text_input("Parameter [A] (Source Column):", placeholder="Contoh: source_country", key="stage2_A")
    with col2:
        B = st.text_input("Parameter [B] (Destination Column):", placeholder="Contoh: destination_country", key="stage2_B")

    if st.button("⚡ Kompilasi & Jalankan Visualisasi Jaringan", key="stage2_run_code"):
        clean_A = A.strip().lower().replace(" ", "_")
        clean_B = B.strip().lower().replace(" ", "_")

        if clean_A == "source_country" and clean_B == "destination_country":
            st.success("✅ Script Sukses Dikompilasi! Merender Topologi Jaringan Global...")

            G = nx.from_pandas_edgelist(df, "source_country", "destination_country")
            degrees = dict(G.degree())

            fig, ax = plt.subplots(figsize=(13, 9), dpi=180)
            apply_cyber_plot_style(fig, ax, bg_color="#040914")

            pos = nx.spring_layout(G, seed=42, k=0.6, iterations=60)

            node_list = list(G.nodes())
            deg_values = [degrees[n] for n in node_list]
            max_deg = max(deg_values) if deg_values else 1

            node_sizes = [max(300, (degrees[n] ** 1.3) * 65) for n in node_list]

            node_colors = []
            for n in node_list:
                if degrees[n] == max_deg or "UNITED STATES" in str(n).upper() or "USA" in str(n).upper():
                    node_colors.append("#fbbf24")
                elif degrees[n] > max_deg * 0.4:
                    node_colors.append("#38bdf8")
                else:
                    node_colors.append("#334155")

            nx.draw_networkx_edges(
                G, pos,
                ax=ax,
                edge_color="#475569",
                alpha=0.35,
                width=1.0,
                arrows=False
            )

            nx.draw_networkx_nodes(
                G, pos,
                ax=ax,
                nodelist=node_list,
                node_color=node_colors,
                node_size=node_sizes,
                alpha=0.9,
                edgecolors="rgba(255,255,255,0.4)",
                linewidths=1.2
            )

            labels = {n: n for n in node_list if degrees[n] > 5}
            nx.draw_networkx_labels(
                G, pos,
                labels=labels,
                ax=ax,
                font_size=8,
                font_color="#f8fafc",
                font_family="sans-serif",
                font_weight="bold"
            )

            ax.set_title("GLOBAL TRANSACTION TOPOLOGY // DEGREE CENTRALITY MAP", fontsize=11, color="#94A3B8", pad=14, fontfamily="monospace")
            ax.axis("off")
            st.pyplot(fig)
            plt.close(fig)

            top_node = max(degrees, key=degrees.get)
            top_deg = degrees[top_node]

            st.markdown(f"""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="term-dot red"></span>
                    <span class="term-dot yellow"></span>
                    <span class="term-dot green"></span>
                    <span class="terminal-title">TOPOLOGY FORENSIC READOUT</span>
                </div>
💡 <b>HINT FORENSIK JARINGAN:</b><br>
• <b>Titik Gravitasi Utama</b> memiliki koneksi degree tertinggi ({top_deg} koneksi langsung).<br>
• Node berukuran paling masif dan berwarna emas merupakan muara akhir dari skema sirkulasi aset.<br>
• Hub teridentifikasi: <b>[CLASSIFIED REGION - DEGREE #{top_deg}]</b>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.error("❌ Parameter Kolom Tidak Valid! Pastikan nama kolom sesuai persis dengan header DataFrame (`source_country` dan `destination_country`).")

    st.markdown('</div>', unsafe_allow_html=True)

    # 8. Final Challenge Section
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Identifikasi Pusat Gravitasi Sistem</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="story-text" style="margin-bottom:1.5rem;">
Berdasarkan peta topologi jaringan di atas, ke negara/entitas manakah seluruh pusaran transaksi ini berkonvergensi?
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input("Masukkan Nama Negara / Node Pusat:", placeholder="Contoh: UNITED STATES", key="stage2_answer")

    if st.button("🚀 Verifikasi Temuan Hub", key="stage2_verify_btn"):
        if validate_stage2_answer(answer):
            st.success("✅ TEPAT! Semua jalur dan koneksi gravitasi mengarah ke UNITED STATES.")
            st.markdown("""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="term-dot red"></span>
                    <span class="term-dot yellow"></span>
                    <span class="term-dot green"></span>
                    <span class="terminal-title">SYS_CONVERGENCE // CONFIRMED</span>
                </div>
&gt; Pola konvergensi berhasil dipetakan.<br>
&gt; Aliran dana melintasi puluhan yurisdiksi sebelum terkonsentrasi di satu titik terminal.<br>
&gt; <i>Membuka berkas investigasi Stage 3: Shadow Access...</i>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.current_stage = 3
            st.rerun()
        else:
            st.error("❌ Belum tepat. Perhatikan node dengan ukuran terbesar dan label paling dominan pada visualisasi graf.")

    st.markdown('</div>', unsafe_allow_html=True)
