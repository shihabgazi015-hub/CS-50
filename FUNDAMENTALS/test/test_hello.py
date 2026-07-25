from hellofunc26 import hello

def tes_default():
    assert hello() == 'Hello, world'

def test_argument():
    assert hello('Shihab') == 'Hello, Shihab'