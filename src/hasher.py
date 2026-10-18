"""Modul untuk hashing password dengan salt (PBKDF2-HMAC-SHA256)."""
import hashlib
import hmac
import secrets
from typing import Optional

ITERATIONS = 200_000


def hash_password(password: str, salt: Optional[bytes] = None) -> str:
    """Hash password. Hasil berformat 'salt$hash' dalam hex."""
    if salt is None:
        salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, ITERATIONS
    )
    return f"{salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    """Cek apakah password cocok dengan hash yang tersimpan."""
    try:
        salt_hex, _ = stored.split("$")
        salt = bytes.fromhex(salt_hex)
    except ValueError:
        return False
    return hmac.compare_digest(hash_password(password, salt), stored)