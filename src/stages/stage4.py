"""
Stage 4: Extraction // Impostor Location
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

from src.components import render_cyber_hud, render_stage_banner, apply_cyber_plot_style
from src.utils import validate_stage4_answer


def stage4_page():
    # 1. Cyber HUD
    render_cyber_hud(current_stage=4)

    # 2. Stage Banner
    ticker_items = [
        {"text": "OVERWRITE ████████", "hot": True},
        {"text": "LEDGER_SHADOW: ACTIVE", "hot": False},
        {"text": "DELTA: [CLASSIFIED]", "warn": True},
        {"text": "ALARM: NONE", "hot": False},
        {"text": "EXTRACTION IN PROGRESS", "hot": True},
        {"text": "GATEWAY_EXT OPENED", "warn": True},
        {"text": "PATH: DETERMINISTIC", "hot": True},
        {"text": "TRAIL: LEFT INTENTIONALLY", "warn": True},
    ]
    render_stage_banner(
        stage_num="04",
        chapter_num="04",
        title_line1="Impostor",
        title_line2="Location",
        accent_color="#f97316",
        meta_tags=["data digantikan", "shadow ledger", "jalur ditinggalkan sengaja", "stage: extraction"],
        ticker_items=ticker_items,
        node_name="NODE_D",
        status_label="RESTRICTED // LVL-4",
    )

    # 3. Hero & Story
    st.markdown("""
    <div class="glass-card hero">
        <div class="main-title">🧩 Stage 4</div>
        <div class="subtitle">Extraction // Impostor Location</div>
        <div class="story-text">
Sistem tidak menunjukkan indikasi kegagalan teknis.
Tidak ada saldo yang tercatat hilang secara nominal.

Namun ketika ledger transaksi lama dibandingkan dengan snapshot ledger baru…
<b>sesuatu tidak cocok.</b>
<hr>
Bukan data yang dihapus secara paksa.
Tapi <b>struktur nilainya yang dialihkan secara terprogram.</b>
<hr>
Semua masih terlihat valid.
Semua transaksi di permukaan masih berjalan normal.

Dan justru kepatuhan terhadap aturan itulah yang membuatnya begitu mematikan.
<hr>
Di antara ratusan transaksi acak (noise), ada satu jalur deterministik berantai
yang menyalurkan nilai secara tersembunyi menuju <b>EXTERNAL_GATEWAY.</b>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 4. Generate & Cache Data Network
    np.random.seed(42)

    nodes = [f"NODE_{i}" for i in range(25)]
    nodes.append("EXTERNAL_GATEWAY")

    paths = []
    for _ in range(500):
        src = np.random.choice(nodes)
        dst = np.random.choice(nodes)
        if src != dst:
            paths.append([src, dst, np.random.randint(100, 900)])

    for _ in range(80):
        paths.append([
            np.random.choice(nodes[:-1]),
            "EXTERNAL_GATEWAY",
            np.random.randint(100, 900)
        ])

    decoy_1 = [
        ("NODE_3", "NODE_6", 510),
        ("NODE_6", "NODE_9", 505),
        ("NODE_9", "NODE_12", 495),
        ("NODE_12", "EXTERNAL_GATEWAY", 500),
    ]

    decoy_2 = [
        ("NODE_10", "NODE_11", 480),
        ("NODE_11", "NODE_12", 485),
        ("NODE_12", "NODE_13", 490),
        ("NODE_13", "EXTERNAL_GATEWAY", 495),
    ]

    clean_path = [
        ("NODE_7", "NODE_14", 331),
        ("NODE_14", "NODE_18", 332),
        ("NODE_18", "NODE_22", 333),
        ("NODE_22", "NODE_5", 334),
        ("NODE_5", "EXTERNAL_GATEWAY", 335),
    ]

    paths += decoy_1 + decoy_2 + clean_path
    df = pd.DataFrame(paths, columns=["source", "destination", "amount"])

    # 5. Live Summary Stat Grid
    st.markdown(f"""
    <div class="stat-grid">
        <div class="stat-box">
            <div class="stat-label">Network Nodes</div>
            <div class="stat-value orange">26 NODES</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Total Pathways</div>
            <div class="stat-value cyan">{len(df)} EDGES</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Target Exit Node</div>
            <div class="stat-value rose">EXTERNAL_GATEWAY</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Deterministic Chain</div>
            <div class="stat-value emerald">5 HOPS ACTIVE</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 6. Graph Build & Visualization
    G = nx.from_pandas_edgelist(
        df,
        "source",
        "destination",
        edge_attr="amount",
        create_using=nx.DiGraph()
    )

    pos = nx.spring_layout(G, seed=42, k=0.85, iterations=80)
    pos["EXTERNAL_GATEWAY"] = np.array([1.0, -0.6])

    clean_values = {331, 332, 333, 334, 335}
    decoy_values = {510, 505, 495, 500, 480, 485, 490}
    clean_signal_nodes = {"NODE_7", "NODE_14", "NODE_18", "NODE_22", "NODE_5"}

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🌐 Visualisasi Topologi Shadow Ledger & Extraction Layer</div>', unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(14, 9), dpi=180)
    apply_cyber_plot_style(fig, ax, bg_color="#040914")

    # Layer 1: Noise Edges
    noise_edges = [
        (u, v) for u, v, d in G.edges(data=True)
        if d["amount"] not in clean_values and d["amount"] not in decoy_values
    ]
    nx.draw_networkx_edges(
        G, pos,
        edgelist=noise_edges,
        edge_color="#334155",
        width=0.7,
        alpha=0.15,
        arrows=False,
        ax=ax
    )

    # Layer 2: Decoy Edges
    decoy_edges = [
        (u, v) for u, v, d in G.edges(data=True)
        if d["amount"] in decoy_values
    ]
    nx.draw_networkx_edges(
        G, pos,
        edgelist=decoy_edges,
        edge_color="#fbbf24",
        width=1.8,
        alpha=0.7,
        arrows=True,
        arrowsize=8,
        ax=ax
    )

    # Layer 3: Clean Deterministic Signal Edges
    clean_edges = [
        (u, v) for u, v, d in G.edges(data=True)
        if d["amount"] in clean_values
    ]
    nx.draw_networkx_edges(
        G, pos,
        edgelist=clean_edges,
        edge_color="#00f0ff",
        width=3.2,
        alpha=0.95,
        arrows=True,
        arrowsize=14,
        ax=ax
    )

    # Nodes styling
    node_colors = []
    node_sizes = []

    for n in G.nodes():
        if n == "EXTERNAL_GATEWAY":
            node_colors.append("#ef4444")
            node_sizes.append(2200)
        elif n in clean_signal_nodes:
            node_colors.append("#06b6d4")
            node_sizes.append(1400)
        elif n in {"NODE_3", "NODE_6", "NODE_9", "NODE_10", "NODE_11", "NODE_12", "NODE_13"}:
            node_colors.append("#f59e0b")
            node_sizes.append(950)
        else:
            node_colors.append("#1e293b")
            node_sizes.append(650)

    nx.draw_networkx_nodes(
        G, pos,
        node_color=node_colors,
        node_size=node_sizes,
        edgecolors="rgba(255,255,255,0.4)",
        linewidths=1.2,
        ax=ax
    )

    nx.draw_networkx_labels(
        G, pos,
        font_size=7.5,
        font_color="#f8fafc",
        font_family="monospace",
        font_weight="bold",
        ax=ax
    )

    ax.set_title("SHADOW LEDGER // DETERMINISTIC EXTRACTION FLOW MAP", fontsize=11, color="#94A3B8", pad=12, fontfamily="monospace")
    ax.axis("off")
    st.pyplot(fig)
    plt.close(fig)

    st.markdown("""
    <div class="terminal">
        <div class="terminal-header">
            <span class="term-dot red"></span>
            <span class="term-dot yellow"></span>
            <span class="term-dot green"></span>
            <span class="terminal-title">FLOW ANALYSIS LOG</span>
        </div>
Dalam jutaan chaos transaksi finansial, terdapat satu pola yang:<br>
• Tidak memiliki volume terbesar secara nominal.<br>
• Tidak memiliki frekuensi tersering.<br>
• <b>Namun paling konsisten secara struktur transfer deterministik.</b><br><br>
Sistem ini tidak menyembunyikan jalurnya — ia hanya menguburnya di bawah jutaan data noise.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # 7. Evaluation Algorithm
    def evaluate_start(node):
        current = node
        score = 0
        signal_nodes = {"NODE_14", "NODE_18", "NODE_22", "NODE_5", "EXTERNAL_GATEWAY"}
        try:
            for _ in range(5):
                next_edges = df[df["source"] == current]
                if next_edges.empty:
                    break
                current = next_edges.sort_values("amount").iloc[0]["destination"]
                if current in signal_nodes:
                    score += 1
        except Exception:
            pass
        return score

    # 8. Final Challenge Section
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Identifikasi Titik Awal Deterministik (Origin Node)</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="story-text" style="margin-bottom:1.5rem;">
Temukan node awal yang memicu rantai ekstraksi deterministik menuju <b>EXTERNAL_GATEWAY</b>:
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input("Masukkan Nama Node Awal:", placeholder="Contoh: NODE_7", key="stage4_answer")

    if st.button("🚀 Analisis Aliran Rantai Deterministik", key="stage4_btn"):
        node_input = answer.strip().upper().replace(" ", "_")
        score = evaluate_start(node_input)

        if validate_stage4_answer(node_input):
            st.success("✔ PATTERN CONFIDENCE: 100% // Rantai Deterministik Sempurna!")
            st.markdown("""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="term-dot red"></span>
                    <span class="term-dot yellow"></span>
                    <span class="term-dot green"></span>
                    <span class="terminal-title">EXTRACTION PATHWAY CONFIRMED</span>
                </div>
&gt; Rantai Deterministik Terdeteksi:<br>
&gt; <b>NODE_7 → NODE_14 → NODE_18 → NODE_22 → NODE_5 → EXTERNAL_GATEWAY</b><br><br>
&gt; <i>Ini bukan sekadar transaksi keuangan...</i><br>
&gt; <i>Ini adalah sistem yang sedang mengarahkan dirinya sendiri untuk berevolusi.</i>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.current_stage = 5
            st.rerun()

        elif score >= 2:
            st.warning("⚠️ PARTIAL MATCH // Anda berada di dekat jalur aliran, tetapi bukan merupakan titik pangkal mula.")
        else:
            st.error("✖ Titik awal tidak terdeteksi dalam pola deterministik. Periksa kembali struktur nilai berurutan pada graf.")

    st.markdown('</div>', unsafe_allow_html=True)
