"""
Legacy adapter for Stage 4. Re-exports stage4_page from src.stages.
"""
from src.stages.stage4 import stage4_page

__all__ = ["stage4_page"]

if __name__ == "__main__":
    import streamlit as st
    stage4_page()