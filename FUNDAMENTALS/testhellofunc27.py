from hellofunc26 import hello

def test_default():
    assert hello() == 'Hello, world'
def test_argument():
    for name in ['Shihab', 'Radia', 'Shafi']:
        assert hello(name) == f'Hello, {name}'
test_default()
test_argument()