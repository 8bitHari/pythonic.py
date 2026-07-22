import pytest

from working import convert


def test_full_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_short_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_mixed_format():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_overnight():
    assert convert("5:00 PM to 9:00 AM") == "17:00 to 09:00"


def test_midnight_and_noon():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_invalid():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 to 5:00")
