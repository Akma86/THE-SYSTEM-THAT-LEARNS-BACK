import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

def stage3_page():

    df_access = pd.read_csv("./data/stage3_access.csv")
    df_system = pd.read_csv("./data/stage3_system.csv")

    df_access['timestamp'] = pd.to_datetime(df_access['timestamp'])
    df_system['timestamp'] = pd.to_datetime(df_system['timestamp'])

    # =========================
    # STORY
    # =========================
    st.markdown("""
    ## 🧩 Stage 3 — Shadow Access

    Semua jejak mengarah ke satu tempat.

    Log akses dibuka.

    Awalnya terlihat normal.

    Namun…

    **ada sesuatu yang tidak masuk akal.**

    > "Semua user masuk lewat login..."
    >  
    > "...atau setidaknya, seharusnya begitu."
    """)

    # =========================
    # DATA
    # =========================
    with st.expander("📂 Access Log"):
        st.dataframe(df_access, use_container_width=True)

    with st.expander("📂 System Log"):
        st.dataframe(df_system, use_container_width=True)

    # =========================
    # VISUAL 1
    # =========================
    st.markdown("### 📊 Aktivitas User")

    df_access['hour'] = df_access['timestamp'].dt.hour

    pivot = df_access.pivot_table(
        index='user_id',
        columns='hour',
        aggfunc='size',
        fill_value=0
    )

    plt.figure(figsize=(12,5))
    sns.heatmap(pivot, cmap="mako")
    st.pyplot(plt)
    plt.clf()

    # =========================
    # 🔥 CORE CLUE
    # =========================
    st.markdown("""
    💡 **Hint:**
    
    Tidak semua yang muncul di access log...
    
    ...pernah benar-benar login.
    """)

    # =========================
    # CHALLENGE
    # =========================
    answer = st.text_input("Siapa user tersebut?")

    if st.button("Kirim"):
        if answer.strip().upper() == "XJ-9A":
            st.success("""
            ...

            "Dia tidak pernah login..."

            "...tapi selalu ada."

            Itu bukan user.

            Itu sesuatu yang lain.
            """)
            time.sleep(1)
            st.session_state.current_stage = 4
            st.rerun()
        else:
            st.error("❌ Salah.")
            time.sleep(1)
            st.rerun()