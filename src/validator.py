"""Modul validasi input pengguna."""

MAX_PASSWORD_LENGTH = 128


def validate_password_input(password: str) -> tuple[bool, str]:
    """Cek input password. Mengembalikan (valid, pesan_error)."""
    if not password or not password.strip():
        return False, "Password tidak boleh kosong"
    if len(password) > MAX_PASSWORD_LENGTH:
        return False, f"Password maksimal {MAX_PASSWORD_LENGTH} karakter"
    if not password.isprintable():
        return False, "Password mengandung karakter yang tidak valid"
    return True, ""


def parse_length(text: str, minimum: int = 8, maximum: int = 64) -> int:
    """Ubah teks jadi panjang password. Raise ValueError jika tidak valid."""
    try:
        value = int(text)
    except ValueError:
        raise ValueError("Panjang harus berupa angka") from None
    if value < minimum or value > maximum:
        raise ValueError(f"Panjang harus antara {minimum} sampai {maximum}")
    return value