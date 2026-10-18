"""Password Toolkit - aplikasi CLI untuk keamanan password."""
import getpass

from src.generator import generate_password
from src.hasher import hash_password, verify_password
from src.strength import get_strength_label, score_password
from src.validator import parse_length, validate_password_input

MENU = """
=== Password Toolkit ===
1. Cek kekuatan password
2. Buat password acak
3. Hash password
4. Verifikasi password
0. Keluar
"""


def ask_password(prompt: str = "Masukkan password: ") -> str:
    """Minta password (input tersembunyi) sampai valid."""
    while True:
        password = getpass.getpass(prompt)
        ok, message = validate_password_input(password)
        if ok:
            return password
        print(f"[!] {message}")


def action_check() -> None:
    password = ask_password()
    print(f"Skor: {score_password(password)}/6 - {get_strength_label(password)}")


def action_generate() -> None:
    try:
        length = parse_length(input("Panjang password (8-64): "))
        result = generate_password(length)
    except ValueError as err:
        print(f"[!] {err}")
        return
    print(f"Password acak: {result}")


def action_hash() -> None:
    password = ask_password()
    print(f"Hash: {hash_password(password)}")


def action_verify() -> None:
    stored = input("Tempel hash (salt$hash): ").strip()
    password = ask_password()
    if verify_password(password, stored):
        print("Password COCOK")
    else:
        print("Password TIDAK cocok")


ACTIONS = {
    "1": action_check,
    "2": action_generate,
    "3": action_hash,
    "4": action_verify,
}


def main() -> None:
    while True:
        print(MENU)
        choice = input("Pilih menu: ").strip()
        if choice == "0":
            print("Sampai jumpa!")
            break
        action = ACTIONS.get(choice)
        if action is None:
            print("[!] Menu tidak valid")
            continue
        action()


if __name__ == "__main__":
    main()