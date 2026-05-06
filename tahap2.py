import streamlit as st
import time
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random

def stage2_page():

    df = pd.read_csv("./data/stage2_network.csv")

    st.markdown("""
    ## 🧩 Stage 2 — Convergence

    Awalnya tidak ada yang aneh.

    Transaksi internasional berjalan seperti biasa.

    Tidak ada pola yang mencurigakan.

    Tidak ada pusat yang terlihat.

    ---

    Namun ketika data divisualisasikan ulang…

    struktur mulai berubah.

    ---

    Bukan karena data berubah.

    Tapi karena cara melihatnya yang berbeda.

    ---

    Beberapa node terlihat lebih “berat” dari yang lain.

    Bukan secara volume.

    Tapi secara koneksi.

    ---

    Dan semakin lama diamati,

    semakin jelas satu hal:

    ---

    Sistem ini tidak tersebar.

    Sistem ini **tertarik ke satu titik.**
    """)
    st.markdown("### 📂 Full Transaction Data")

    st.dataframe(df, use_container_width=True)
    # =========================
    # INPUT KOORDINAT (FINAL ANSWER)
    # =========================
    st.markdown("### 🎯 Identifikasi Pusat Sistem")

    answer = st.text_input("Ke mana semua jalur ini sebenarnya mengarah?")

    if st.button("Kirim Jawaban"):
        if "UNITED STATES" in answer.upper() or "US" in answer.upper():
            st.success("✅ Benar. Semua jalur mengarah ke sana.")
            time.sleep(1)
            st.session_state.current_stage = 3
            st.rerun()
        else:
            st.error("❌ Salah. Perhatikan pola koneksi.")
            time.sleep(1)
            st.rerun()

    # =========================
    # ANALISIS SECTION
    # =========================
    st.markdown("## 🔍 Analisis Jaringan")

    st.markdown("""
    Seorang analis mencoba memvisualisasikan jaringan transaksi.

    Namun… kode yang digunakan tidak lengkap.
    """)

    st.code("""
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.from_pandas_edgelist(df, '...[A]...', '...[B]...')

    pos = nx.spring_layout(G, seed=42)

    degree = dict(G.degree())
    node_sizes = [degree[n]*60 for n in G.nodes()]

    nx.draw(
        G, pos,
        with_labels=True,
        node_size=node_sizes
    )

    plt.show()
""")

    st.markdown("### Lengkapi kode:")

    A = st.text_input("Isi A (source):")
    B = st.text_input("Isi B (destination):")

    if st.button("Run Code"):
        if A == "source_country" and B == "destination_country":

            st.success("Visualisasi berhasil dijalankan...")

            # =========================
            # VISUALISASI
            # =========================
            G = nx.from_pandas_edgelist(df, 'source_country', 'destination_country')

            plt.figure(figsize=(12,10))
            pos = nx.spring_layout(G, seed=42)

            # warna random
            color_map = {node:(random.random(),random.random(),random.random()) for node in G.nodes()}
            node_colors = [color_map[node] for node in G.nodes()]

            # size = degree
            degree = dict(G.degree())
            node_sizes = [degree[n]*80 for n in G.nodes()]

            nx.draw(
                G, pos,
                with_labels=True,
                node_color=node_colors,
                node_size=node_sizes,
                font_size=8,
                edge_color="gray",
                alpha=0.6
            )

            st.pyplot(plt)
            plt.clf()

            # =========================
            # HINT HALUS
            # =========================
            st.markdown("""
            💡 **Hint:**
            - Node terbesar = pusat aliran  
            - Perhatikan koneksi terbanyak  
            """)

        else:
            st.error("❌ Code Error! Periksa kembali nama kolom.")