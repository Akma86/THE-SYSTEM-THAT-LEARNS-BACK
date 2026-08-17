"""
Legacy adapter for Stage 3. Re-exports stage3_page from src.stages.
"""
from src.stages.stage3 import stage3_page

__all__ = ["stage3_page"]

if __name__ == "__main__":
    import streamlit as st
    stage3_page()