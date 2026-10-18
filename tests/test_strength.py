from src.strength import get_strength_label, score_password


def test_weak_list_scores_zero():
    assert score_password("password") == 0


def test_short_password_is_weak():
    assert get_strength_label("abc") == "Lemah"


def test_medium_password():
    assert get_strength_label("Abcd1234") == "Sedang"


def test_strong_password():
    assert get_strength_label("Abc123!xyz789") == "Kuat"