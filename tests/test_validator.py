import pytest

from src.validator import parse_length, validate_password_input


def test_empty_password_invalid():
    assert validate_password_input("   ")[0] is False


def test_too_long_password_invalid():
    assert validate_password_input("a" * 129)[0] is False


def test_valid_password():
    assert validate_password_input("Abc12345!") == (True, "")


def test_parse_length_valid():
    assert parse_length("12") == 12


def test_parse_length_not_a_number():
    with pytest.raises(ValueError):
        parse_length("abc")


def test_parse_length_out_of_range():
    with pytest.raises(ValueError):
        parse_length("100")