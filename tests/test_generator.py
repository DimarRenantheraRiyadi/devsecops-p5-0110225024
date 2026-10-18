import pytest

from src.generator import generate_password


def test_default_length():
    assert len(generate_password()) == 16


def test_custom_length_without_symbols():
    result = generate_password(20, use_symbols=False)
    assert len(result) == 20
    assert result.isalnum()


def test_too_short_raises_error():
    with pytest.raises(ValueError):
        generate_password(4)


def test_passwords_are_random():
    assert generate_password() != generate_password()