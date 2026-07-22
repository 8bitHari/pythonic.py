from datetime import date, timedelta

from seasons import get_minutes


def test_same_day():
    assert get_minutes(date.today()) == 0


def test_one_day():
    yesterday = date.today() - timedelta(days=1)
    assert get_minutes(yesterday) == 24 * 60


def test_one_year():
    one_year_ago = date.today() - timedelta(days=365)
    assert get_minutes(one_year_ago) == 365 * 24 * 60
