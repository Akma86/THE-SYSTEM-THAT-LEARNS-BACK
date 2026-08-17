"""
Legacy adapter for Stage 1. Re-exports stage1_page from src.stages.
"""
from src.stages.stage1 import stage1_page

__all__ = ["stage1_page"]

if __name__ == "__main__":
    import streamlit as st
    stage1_page()