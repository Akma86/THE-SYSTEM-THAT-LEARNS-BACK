"""
Stage 2: Convergence // Shadows in the Sky
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
        title_line1="Shadows",
        title_line2="In The Sky",
        accent_color="#f59e0b",
        meta_tags=["all paths → single node", "shadow architecture", "cross-border routing", "unregistered"],
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
        <div class="subtitle">Convergence // Shadows in the Sky</div>
        <div class="story-text">
At first glance, nothing appears anomalous.

International wire transactions execute within normal variance parameters.
No blatant routing loops.
No obvious single bottleneck visible on raw tables.
<hr>
Yet when the dataset is projected onto a topological graph…
<b>the underlying geometry transforms.</b>
<hr>
Not because the transactions changed.
Rather because <b>the vantage point reveals gravitational pull.</b>
<hr>
Certain nodes carry disproportionate weight compared to the rest.
Not solely by nominal transaction volume…
but by <b>global connection degree centrality.</b>
<hr>
And the longer one observes the topology, the clearer the reality becomes:
This capital network is not decentralized.
It is <b>irrevocably pulled toward a single gravitational center.</b>
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
    st.markdown('<div class="section-title">📂 Global Cross-Border Transaction Matrix</div>', unsafe_allow_html=True)

    st.dataframe(df, use_container_width=True, height=280)
    st.markdown('</div>', unsafe_allow_html=True)

    # 7. Code Reconstruction & Network Visualization Section
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔍 Graph Visualization Script Reconstruction</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="story-text" style="margin-bottom:1.5rem;">
A forensic analyst previously attempted to map this network, but their script was left incomplete at the edge list definition.
Supply the missing DataFrame column parameters to compile the network graph:
    </div>
    """, unsafe_allow_html=True)

    st.code("""
import networkx as nx
import matplotlib.pyplot as plt

# Construct edge list from DataFrame columns
G = nx.from_pandas_edgelist(df, source='...[A]...', target='...[B]...')

pos = nx.spring_layout(G, seed=42)
degree = dict(G.degree())
node_sizes = [degree[n] * 70 for n in G.nodes()]

nx.draw(G, pos, with_labels=True, node_size=node_sizes)
plt.show()
""", language="python")

    st.markdown('<div class="section-title" style="font-size:1.3rem; margin-top:1.5rem;">💻 Parameter Injection Fields</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        A = st.text_input("Parameter [A] (Source Column):", placeholder="e.g. source_country", key="stage2_A")
    with col2:
        B = st.text_input("Parameter [B] (Destination Column):", placeholder="e.g. destination_country", key="stage2_B")

    if st.button("⚡ Compile & Render Network Topology", key="stage2_run_code"):
        clean_A = A.strip().lower().replace(" ", "_")
        clean_B = B.strip().lower().replace(" ", "_")

        if clean_A == "source_country" and clean_B == "destination_country":
            st.success("✅ Script Compiled Successfully! Rendering Global Graph Topology...")

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
💡 <b>NETWORK FORENSIC HINT:</b><br>
• <b>Primary Gravitational Hub</b> exhibits the highest degree centrality ({top_deg} direct connections).<br>
• The largest golden node serves as the ultimate destination for cross-border capital circulation.<br>
• Identified Central Hub: <b>[CLASSIFIED REGION - DEGREE #{top_deg}]</b>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.error("❌ Column parameter error! Ensure names match the exact DataFrame headers (`source_country` and `destination_country`).")

    st.markdown('</div>', unsafe_allow_html=True)

    # 8. Final Challenge Section
    st.markdown('<div class="glass-card hero">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Identify the Gravitational Hub</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="story-text" style="margin-bottom:1.5rem;">
Based on the topological graph rendered above, which nation/entity acts as the focal center of convergence?
    </div>
    """, unsafe_allow_html=True)

    answer = st.text_input("Enter Country / Hub Name:", placeholder="e.g. UNITED STATES", key="stage2_answer")

    if st.button("🚀 Verify Central Hub", key="stage2_verify_btn"):
        if validate_stage2_answer(answer):
            st.success("✅ CORRECT! All topological trajectories converge toward UNITED STATES.")
            st.markdown("""
            <div class="terminal">
                <div class="terminal-header">
                    <span class="term-dot red"></span>
                    <span class="term-dot yellow"></span>
                    <span class="term-dot green"></span>
                    <span class="terminal-title">SYS_CONVERGENCE // CONFIRMED</span>
                </div>
&gt; Convergence pattern mapped.<br>
&gt; Capital flows across dozens of legal jurisdictions before accumulating into a terminal node.<br>
&gt; <i>Accessing Stage 3 dossier: Shadow Access...</i>
            </div>
            """, unsafe_allow_html=True)

            st.session_state.current_stage = 3
            st.rerun()
        else:
            st.error("❌ Incorrect. Scrutinize the node with highest degree centrality and prominent label in the graph.")

    st.markdown('</div>', unsafe_allow_html=True)
