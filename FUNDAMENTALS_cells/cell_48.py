n = int(input("tell me - "))
def main(m):

  print_square1(m)
  print("\nNew code\n")
  print_square2(m)
  print("\nNew code\n")
  print_square3(m)

def print_square1(size):
  for i in range(size):

    for j in range(size):
      # print(brick)
      print('#')

def print_square2(size):

  # for each brick in row
  for i in range(size):

    for j in range(size):
      # print(brick)
      print('#', end = '')


# for each row in square
def print_square3(size):

  # for each brick in row
  for i in range(size):

    for j in range(size):
      # print(brick)
      print('#', end = '')
    print()

main(n)