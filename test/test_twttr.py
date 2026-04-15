from twttr_new import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("CS50") == "CS50"
    assert shorten("Hello, World!") == "Hll, Wrld!"