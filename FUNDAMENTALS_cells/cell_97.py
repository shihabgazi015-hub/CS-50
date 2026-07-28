%%writefile test_calculator.py

from calculator import square

# standard pytest functions just sit at the top level
def test_square():
  assert square(2) == 4
  assert square(3) == 9
  assert square(-2) == 4
  assert square(-3) == 9
  assert square(0) == 0