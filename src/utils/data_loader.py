"""
Dataset loaders with Streamlit caching for maximum performance.
"""
import streamlit as st
import pandas as pd
from pathlib import Path
from src.config import DATA_PATHS


@st.cache_data(show_spinner=False)
def load_stage1_data() -> pd.DataFrame:
    """Loads Stage 1 noise dataset."""
    path = DATA_PATHS["stage1"]
    return pd.read_csv(path)


@st.cache_data(show_spinner=False)
def load_stage2_data() -> pd.DataFrame:
    """Loads Stage 2 cross-border network dataset."""
    path = DATA_PATHS["stage2_network"]
    return pd.read_csv(path)


@st.cache_data(show_spinner=False)
def load_stage3_data():
    """Loads Stage 3 access logs and system security logs."""
    access_path = DATA_PATHS["stage3_access"]
    system_path = DATA_PATHS["stage3_system"]
    df_access = pd.read_csv(access_path)
    df_system = pd.read_csv(system_path)
    df_access["timestamp"] = pd.to_datetime(df_access["timestamp"])
    df_system["timestamp"] = pd.to_datetime(df_system["timestamp"])
    return df_access, df_system


@st.cache_data(show_spinner=False)
def load_paths_data() -> pd.DataFrame:
    """Loads paths dataset."""
    path = DATA_PATHS["paths"]
    return pd.read_csv(path)
