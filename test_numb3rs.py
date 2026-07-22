from numb3rs import validate


def test_valid():
    assert validate("0.0.0.0") is True
    assert validate("255.255.255.255") is True
    assert validate("192.168.1.1") is True


def test_out_of_range():
    assert validate("275.3.6.28") is False
    assert validate("256.1.1.1") is False


def test_invalid_format():
    assert validate("1.2.3") is False
    assert validate("1.2.3.4.5") is False
    assert validate("cat") is False
