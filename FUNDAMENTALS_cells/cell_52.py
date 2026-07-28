try:
  x = int(input("What's x?\n"))
  print(f'x is {x}')
except ValueError:
  print("x should be an integer")