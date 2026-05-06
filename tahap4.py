def stage4_page():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import networkx as nx
    import time

    st.markdown("""
    ## 🧩 Stage 4 — Extraction

    Sistem tidak menunjukkan kegagalan.

    Tidak ada transaksi yang hilang.

    Namun ketika ledger lama dibandingkan dengan snapshot baru…

    sesuatu tidak cocok.

    Bukan data yang hilang.

    Tapi **struktur nilainya yang berubah.**
    """)

    # =========================
    # DATA GENERATION
    # =========================
    np.random.seed(42)

    nodes = [f"NODE_{i}" for i in range(25)]
    nodes.append("EXTERNAL_GATEWAY")

    paths = []

    # =========================
    # CHAOS LAYER (NOISE)
    # =========================
    for _ in range(500):
        src = np.random.choice(nodes)
        dst = np.random.choice(nodes)

        if src != dst:
            paths.append([src, dst, np.random.randint(100, 900)])

    # =========================
    # GATEWAY NOISE
    # =========================
    for _ in range(80):
        paths.append([
            np.random.choice(nodes[:-1]),
            "EXTERNAL_GATEWAY",
            np.random.randint(100, 900)
        ])

    # =========================
    # DECOY CHAINS (FAKE PATTERNS)
    # =========================
    decoy_1 = [
        ("NODE_3","NODE_6",510),
        ("NODE_6","NODE_9",505),
        ("NODE_9","NODE_12",495),
        ("NODE_12","EXTERNAL_GATEWAY",500)
    ]

    decoy_2 = [
        ("NODE_10","NODE_11",480),
        ("NODE_11","NODE_12",485),
        ("NODE_12","NODE_13",490),
        ("NODE_13","EXTERNAL_GATEWAY",495)
    ]

    # =========================
    # REAL CLEAN PATH (HIDDEN SIGNAL)
    # =========================
    clean_path = [
        ("NODE_7","NODE_14",331),
        ("NODE_14","NODE_18",332),
        ("NODE_18","NODE_22",333),
        ("NODE_22","NODE_5",334),
        ("NODE_5","EXTERNAL_GATEWAY",335)
    ]

    paths += decoy_1 + decoy_2 + clean_path

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

    # gateway positioning
    pos["EXTERNAL_GATEWAY"] = [1.0, -0.6]

    # =========================
    # EDGE CLASSIFICATION
    # =========================
    clean_values = [331,332,333,334,335]
    decoy_values = [510,505,495,500,480,485,490]

    edge_colors = []
    edge_widths = []
    edge_alpha = []

    for u, v, d in G.edges(data=True):
        amt = d["amount"]

        if amt in clean_values:
            edge_colors.append("#4fc3f7")
            edge_widths.append(np.random.uniform(2.5, 3.5))
            edge_alpha.append(np.random.uniform(0.6, 0.95))

        elif amt in decoy_values:
            edge_colors.append("#ffd54f")
            edge_widths.append(np.random.uniform(1.8, 2.5))
            edge_alpha.append(np.random.uniform(0.4, 0.7))

        else:
            edge_colors.append("#9e9e9e")
            edge_widths.append(np.random.uniform(0.2, 0.8))
            edge_alpha.append(np.random.uniform(0.05, 0.2))

    # =========================
    # VISUALIZATION
    # =========================
    plt.figure(figsize=(16,10))

    # noise layer
    for (u, v), c, w, a in zip(G.edges(), edge_colors, edge_widths, edge_alpha):
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[(u, v)],
            edge_color=c,
            width=w,
            alpha=a,
            arrows=False
        )

    # signal layer
    for (u, v, d), c, w, a in zip(G.edges(data=True), edge_colors, edge_widths, edge_alpha):
        if d["amount"] in clean_values:
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=[(u, v)],
                edge_color=c,
                width=w,
                alpha=0.9,
                arrows=True,
                arrowsize=10
            )

    # =========================
    # NODE STYLE (SUBTLE CLUSTERING)
    # =========================
    node_colors = []
    node_sizes = []

    for n in G.nodes():
        if n == "EXTERNAL_GATEWAY":
            node_colors.append("#2c3e50")
            node_sizes.append(2500)

        elif n in ["NODE_7","NODE_14","NODE_18","NODE_22","NODE_5"]:
            node_colors.append("#ff6b6b")
            node_sizes.append(1300)

        else:
            node_colors.append("#3498db")
            node_sizes.append(np.random.randint(900,1100))

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes)

    nx.draw_networkx_labels(G, pos, font_size=7)

    plt.title("Shadow Ledger — Extraction Layer", fontsize=14)
    plt.axis("off")

    st.pyplot(plt)
    plt.clf()

    # =========================
    # STORY CLUE
    # =========================
    st.markdown("""
    ## 🔍 System Observation

    Dalam chaos transaksi, terdapat satu pola yang:

    - tidak paling besar
    - tidak paling sering
    - tidak paling mencolok

    Tapi **paling konsisten secara struktur aliran.**

    ---
    """)

    # =========================
    # SCORING SYSTEM (NOT JUST ANSWER)
    # =========================
    def evaluate_start(node):
        current = node
        score = 0

        try:
            for _ in range(5):
                next_edges = df[df["source"] == current]

                if len(next_edges) == 0:
                    break

                # pilih path paling stabil (lowest variance approach)
                next_node = next_edges.sort_values("amount").iloc[0]["destination"]

                current = next_node

                if current in ["NODE_14","NODE_18","NODE_22","NODE_5","EXTERNAL_GATEWAY"]:
                    score += 1

        except:
            pass

        return score

    # =========================
    # INPUT (MORE INTELLIGENT)
    # =========================
    answer = st.text_input("Identify origin node of deterministic flow:")

    if st.button("Analyze"):

        score = evaluate_start(answer.strip().upper())

        if score >= 4:
            st.success("""
            ✔ Pattern Confidence High

            Deterministic chain detected:

            NODE_7 → NODE_14 → NODE_18 → NODE_22 → NODE_5 → EXTERNAL_GATEWAY

            Ini bukan transaksi.

            Ini sistem yang sedang mengarahkan dirinya sendiri.
            """)

            time.sleep(2)
            st.session_state.current_stage = 5
            st.rerun()

        elif score >= 2:
            st.warning("""
            ⚠ Partial Match

            Anda berada di dekat jalur yang benar.

            Tapi sistem ini tidak memiliki satu titik awal yang jelas.
            """)

        else:
            st.error("""
            ✖ No deterministic structure found.

            Sistem tetap terlihat acak.
            Tapi mungkin Anda belum melihat cukup dalam.
            """)