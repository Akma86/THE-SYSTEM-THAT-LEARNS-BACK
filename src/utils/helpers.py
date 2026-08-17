"""
Validation and utility helpers for game evaluation.
"""
import re


def normalize_text(text: str) -> str:
    """Normalizes input string for forgiving validation (removes punctuation, extra spaces, upper)."""
    if not text:
        return ""
    cleaned = re.sub(r"[^\w\s]", "", text)
    return " ".join(cleaned.strip().upper().split())


def validate_stage1_answer(answer: str) -> bool:
    """Validates Stage 1 ASCII cipher answer."""
    normalized = normalize_text(answer)
    valid = ["YOU ARE LATE", "YOU WERE LATE", "YOURE LATE"]
    return normalized in valid


def validate_stage2_answer(answer: str) -> bool:
    """Validates Stage 2 central hub answer."""
    normalized = normalize_text(answer)
    valid_keywords = ["UNITED STATES", "USA", "US", "AMERIKA SERIKAT", "AMERIKA"]
    return any(kw in normalized for kw in valid_keywords)


def validate_stage3_answer(answer: str) -> bool:
    """Validates Stage 3 ghost user answer."""
    normalized = normalize_text(answer).replace("USER", "").strip()
    return normalized in ["XJ9A", "XJ 9A", "XJ9 A"]


def validate_stage4_answer(answer: str) -> bool:
    """Validates Stage 4 origin node answer."""
    normalized = normalize_text(answer).replace(" ", "_")
    return normalized in ["NODE_7", "NODE7", "7", "N7"]
