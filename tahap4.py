def stage4_page():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    import time

    # =========================
    # STORY HEADER
    # =========================
    st.markdown("""
    ## 🧩 Stage 4 — Extraction

    Ketika mereka menyadari apa yang terjadi—  
    semuanya sudah terlambat.

    Tidak ada alarm.  
    Tidak ada indikasi.

    Hanya satu hal yang terlihat:

    **saldo tidak berubah… tapi nilai sudah hilang.**
    """)

    # =========================
    # DATA GENERATION
    # =========================
    np.random.seed(42)

    nodes = [f"NODE_{i}" for i in range(25)]
    nodes.append("EXTERNAL_GATEWAY")

    paths = []

    # 🔊 NOISE (CHAOS LAYER)
    for _ in range(400):
        src = np.random.choice(nodes)
        dst = np.random.choice(nodes)
        if src != dst:
            paths.append([src, dst, np.random.randint(100, 900)])

    # 🔁 GATEWAY NOISE
    for _ in range(80):
        paths.append([
            np.random.choice(nodes[:-1]),
            "EXTERNAL_GATEWAY",
            np.random.randint(100, 900)
        ])

    # ⚠️ DECOY PATH
    decoy = [
        ("NODE_3","NODE_6",510),
        ("NODE_6","NODE_9",505),
        ("NODE_9","NODE_12",495),
        ("NODE_12","EXTERNAL_GATEWAY",500)
    ]

    # 🔥 CLEAN PATH (REAL ANSWER)
    clean = [
        ("NODE_7","NODE_14",331),
        ("NODE_14","NODE_18",332),
        ("NODE_18","NODE_22",333),
        ("NODE_22","NODE_5",334),
        ("NODE_5","EXTERNAL_GATEWAY",335)
    ]

    paths += decoy + clean

    df = pd.DataFrame(paths, columns=["source","destination","amount"])

    # =========================
    # GRAPH BUILD
    # =========================
    G = nx.from_pandas_edgelist(
        df,
        "source",
        "destination",
        edge_attr="amount",
        create_using=nx.DiGraph()
    )

    pos = nx.spring_layout(G, seed=42, k=0.8, iterations=80)

    # pin gateway
    pos["EXTERNAL_GATEWAY"] = [1.0, -0.6]

    # =========================
    # EDGE STYLE — FORENSIC CHAOS MODE
    # =========================
    edge_colors = []
    edge_widths = []
    edge_alphas = []

    for u, v, d in G.edges(data=True):
        amt = d["amount"]

        # CLEAN PATH
        if amt in [331,332,333,334,335]:
            edge_colors.append("#4fc3f7")
            edge_widths.append(np.random.uniform(2.2, 3.2))
            edge_alphas.append(np.random.uniform(0.6, 0.95))

        # DECOY
        elif amt in [510,505,495,500]:
            edge_colors.append("#ffd54f")
            edge_widths.append(np.random.uniform(1.8, 2.5))
            edge_alphas.append(np.random.uniform(0.5, 0.8))

        # NOISE
        else:
            edge_colors.append("#9e9e9e")
            edge_widths.append(np.random.uniform(0.3, 1.0))
            edge_alphas.append(np.random.uniform(0.05, 0.2))

    # =========================
    # DRAW GRAPH (LAYERED)
    # =========================
    plt.figure(figsize=(15,10))

    # layer 1: noise (no direction)
    for (u, v), c, w, a in zip(G.edges(), edge_colors, edge_widths, edge_alphas):
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[(u, v)],
            edge_color=c,
            width=w,
            alpha=a,
            arrows=False
        )

    # layer 2: signal (directed)
    for (u, v, d), c, w, a in zip(G.edges(data=True), edge_colors, edge_widths, edge_alphas):
        if d["amount"] in [331,332,333,334,335] or d["amount"] in [510,505,495,500]:
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=[(u, v)],
                edge_color=c,
                width=w,
                alpha=min(1.0, a + 0.2),
                arrows=True,
                arrowsize=10
            )

    # =========================
    # NODE STYLE
    # =========================
    node_colors = []
    node_sizes = []

    for n in G.nodes():
        if n == "EXTERNAL_GATEWAY":
            node_colors.append("#1a1a1a")
            node_sizes.append(2800)

        elif n.startswith("NODE_7") or n in ["NODE_7","NODE_14","NODE_18","NODE_22","NODE_5"]:
            node_colors.append("#ff6b6b")
            node_sizes.append(1200)

        else:
            node_colors.append("#3498db")
            node_sizes.append(np.random.randint(900, 1100))

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)

    # labels
    nx.draw_networkx_labels(G, pos, font_size=7, font_color="white")

    plt.title("Shadow Ledger — Extraction Layer", fontsize=14)
    plt.axis("off")

    st.pyplot(plt)
    plt.clf()

    # =========================
    # UX CLUE TEXT
    # =========================
    st.markdown("""
    ## 🔍 System Observation

    Tidak semua jalur memiliki noise yang sama.

    Ada satu jalur yang:
    - stabil
    - konsisten
    - terlalu “bersih”

    Sistem tidak menghapusnya.

    Sistem justru membiarkannya terlihat.
    """)

    # =========================
    # INPUT (SLIGHTLY HARDER UX)
    # =========================
    answer = st.text_input("Identify the origin node of the extraction path:")

    hint = st.expander("Hint (optional)")
    with hint:
        st.write("""
        Semua aliran besar selalu dimulai dari titik yang paling awal muncul dalam struktur stabil.
        """)

    if st.button("Submit"):
        if answer.strip().upper() == "NODE_7":
            st.success("""
            ✔ Pattern confirmed

            NODE_7 → NODE_14 → NODE_18 → NODE_22 → NODE_5 → EXTERNAL_GATEWAY

            Ini bukan transaksi.

            Ini ekstraksi sistemik.
            """)
            time.sleep(2)
            st.session_state.current_stage = 5
            st.rerun()
        else:
            st.error("Pattern mismatch. Try re-evaluating stable flow nodes.")