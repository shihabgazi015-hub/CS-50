try:
  x = int(input("What's x?\n"))
except ValueError:
  print("x should be an integer")
else:
  print(f'x is {x}')