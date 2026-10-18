"""Modul untuk mengecek kekuatan password."""
import re

# Daftar password yang terlalu umum dan mudah ditebak
WEAK_LIST = {
    "password", "123456", "12345678", "qwerty",
    "admin", "letmein", "welcome", "abc123",
}


def score_password(password: str) -> int:
    """Hitung skor password dari 0 sampai 6."""
    if password.lower() in WEAK_LIST:
        return 0

    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    return score


def get_strength_label(password: str) -> str:
    """Ubah skor menjadi label: Lemah, Sedang, atau Kuat."""
    score = score_password(password)
    if score <= 2:
        return "Lemah"
    if score <= 4:
        return "Sedang"
    return "Kuat"