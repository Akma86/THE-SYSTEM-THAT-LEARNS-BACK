import os
from pathlib import Path

# Base Directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"

# Data File Paths
DATA_PATHS = {
    "stage1": DATA_DIR / "stage1.csv",
    "stage2_network": DATA_DIR / "stage2_network.csv",
    "stage3_access": DATA_DIR / "stage3_access.csv",
    "stage3_system": DATA_DIR / "stage3_system.csv",
    "paths": DATA_DIR / "paths.csv",
    "access_log": DATA_DIR / "access_log.csv",
    "ledger_old": DATA_DIR / "ledger_old.csv",
    "ledger_new": DATA_DIR / "ledger_new.csv",
}

# Asset Paths
ASSET_PATHS = {
    "ascii_art": ASSETS_DIR / "ascii.png",
    "logo": ASSETS_DIR / "Big Data Logo.png",
    "cover_banner": ASSETS_DIR / "BDgamecover.png",
    "banner_1": ASSETS_DIR / "1.png",
    "banner_2": ASSETS_DIR / "2.png",
    "banner_3": ASSETS_DIR / "3.png",
    "banner_4": ASSETS_DIR / "4.png",
    "denah": ASSETS_DIR / "Denah.png",
}

# Game Configuration
GAME_CONFIG = {
    "title": "The System That Learns Back",
    "subtitle": "A Cyber Investigation & Data Forensics Experience",
    "organization": "Big Data Happiness · MBC Investigation Unit",
    "version": "2.4.0",
    "kaggle_archive_url": "https://www.kaggle.com/t/afff427d24eb46709efc594b4f36394c",
    "total_stages": 7,
}
