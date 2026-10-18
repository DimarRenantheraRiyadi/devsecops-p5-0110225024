from src.hasher import hash_password, verify_password


def test_hash_format_has_salt_and_digest():
    salt_hex, digest_hex = hash_password("Rahasia123!").split("$")
    assert len(salt_hex) == 32
    assert len(digest_hex) == 64


def test_verify_correct_password():
    stored = hash_password("Rahasia123!")
    assert verify_password("Rahasia123!", stored) is True


def test_verify_wrong_password():
    stored = hash_password("Rahasia123!")
    assert verify_password("salah", stored) is False


def test_same_password_gives_different_hash():
    assert hash_password("abc12345") != hash_password("abc12345")


def test_invalid_stored_format_returns_false():
    assert verify_password("abc", "bukan-hash") is False