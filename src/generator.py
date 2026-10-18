"""Modul untuk membuat password acak yang aman."""
import secrets
import string


def generate_password(length: int = 16, use_symbols: bool = True) -> str:
    """Buat password acak memakai modul secrets (aman untuk keperluan keamanan)."""
    if length < 8:
        raise ValueError("Panjang password minimal 8 karakter")

    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+"

    return "".join(secrets.choice(alphabet) for _ in range(length))