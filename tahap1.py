def stage1_page():
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import time

    # =========================
    # STYLE
    # =========================
    hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body {display: flex; justify-content: center; align-items: center;}
    </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # =========================
    # LOAD DATA
    # =========================
    df = pd.read_csv("./data/stage1.csv")

    # =========================
    # STORY
    # =========================
    st.markdown("""
    ## 🧩 Stage 1 — Noise

    Malam itu, sistem keuangan nasional berjalan seperti biasa.

    Tidak ada gangguan.
    Tidak ada alarm.
    Tidak ada alasan untuk khawatir.

    Setidaknya… di permukaan.

    ---

    Transaksi mengalir seperti setiap hari.
    Angka naik dan turun sesuai pola yang bisa diprediksi.

    Semuanya terlihat stabil.

    Terlalu stabil.

    ---

    Seorang analis membuka dashboard utama.

    Ia berhenti.

    Bukan karena ada error.

    Tapi karena…
    sesuatu terlihat terlalu “rapi”.

    ---

    Dalam lautan data yang bergerak acak,
    ada satu bagian yang tidak ikut bergerak.

    Tidak mencolok.
    Tidak mencurigakan.

    Hanya… berbeda.

    ---

    Dan di sistem yang seharusnya tidak punya ingatan,

    bagian itu terasa seperti sesuatu yang sedang menunggu untuk dikenali.
    """)

    # =========================
    # 📈 VISUALISASI UTAMA
    # =========================
    st.markdown("### 📊 Grafik Transaksi")

    plt.figure(figsize=(12,6))

    for col in df.columns[1:]:
        plt.plot(df["time"], df[col], alpha=0.6)

    plt.title("Pergerakan Semua Account")
    plt.xlabel("Time")
    plt.ylabel("Value")

    st.pyplot(plt.gcf())
    plt.clf()

    # =========================
    # 🧠 ANALISIS TOOL
    # =========================
    st.markdown("## 🔍 Analisis Data")

    option = st.radio(
        "Pilih alat analisis:",
        ["Heatmap Korelasi", "Lihat Data Penuh"]
    )

    # =========================
    # HEATMAP (HINT HALUS)
    # =========================
    if option == "Heatmap Korelasi":
        st.markdown("""
        ### 🔥 Korelasi Antar Account
        
        > Tidak semua yang berbeda itu mencolok.  
        > Kadang… justru yang paling “tenang”.
        """)
        
        corr = df.drop(columns="time").corr()

        plt.figure(figsize=(10,8))
        sns.heatmap(corr, annot=True, cmap="coolwarm")
        st.pyplot(plt.gcf())
        plt.clf()

    # =========================
    # KOMPARASI (KUNCI)
    # =========================
    elif option == "Lihat Data Penuh":
        st.markdown("""
        ### 📋 Data Lengkap
        
        > Kadang jawabannya tidak muncul dari perbandingan…  
        > tapi dari melihat semuanya sekaligus.
        
        Tidak ada yang disembunyikan.  
        **Hanya perlu cara melihatnya.**
        """)

        st.dataframe(df, use_container_width=True)

        st.markdown("""
        💡 Hint tambahan:  
        Tidak semua anomali terlihat seperti error.

        Beberapa justru terlihat seperti keteraturan.
        """)

    # =========================
    # 🎯 INPUT JAWABAN
    # =========================
    from PIL import Image
    image3 = Image.open("assets/ascii.png")
    try:
        st.image(image3, caption='', use_container_width=True)
    except TypeError:
        st.image(image3, caption='', use_column_width=True)
        
    st.markdown("## 🎯 Temukan Pesan Tersembunyi")

    answer = st.text_input("Masukkan kata yang kamu temukan:")

    if st.button("Kirim"):
        if answer.strip().upper() == "YOU ARE LATE":
            st.success("...")

            st.markdown("""
            Layar berkedip.

            Satu baris teks muncul.

            “YOU ARE LATE.”

            Tidak ada konteks.
            Tidak ada sumber.

            Dan untuk pertama kalinya—
            sistem tidak mencoba menjelaskan apa pun.
            """)

            time.sleep(2)
            st.session_state.current_stage = 2
            st.rerun()
        else:
            st.error("❌ Tidak tepat...")
            time.sleep(1)
            st.warning("Sistem mengulang analisis...")
            st.rerun()