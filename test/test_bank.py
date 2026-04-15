from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("what's up?") == 100
    assert value("HELLO") == 0