n = int(input("tell me - "))
def main(m):
  print_square(m)

def print_square(size):
  for i in range(size):
    print_row(size)

def print_row(width):
  print('#' *width)
main(n)