"""
Legacy adapter for Stage 2. Re-exports stage2_page from src.stages.
"""
from src.stages.stage2 import stage2_page

__all__ = ["stage2_page"]

if __name__ == "__main__":
    import streamlit as st
    stage2_page()