from unit_tests import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    for i in range (10000000000000000000000000000000000000000):
        assert square(i) == i*i