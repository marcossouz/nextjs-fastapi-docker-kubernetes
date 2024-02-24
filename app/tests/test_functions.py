from app.functions import get_random_number


def test_get_random_number():
    assert 0 <= get_random_number()
    assert get_random_number() < 10
