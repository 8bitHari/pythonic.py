from um import count


def test_single():
    assert count("hello, um, world") == 1


def test_none():
    assert count("yummy") == 0


def test_multiple():
    assert count("um, this is, um, tricky") == 2


def test_case_insensitive():
    assert count("Um, what? UM.") == 2
