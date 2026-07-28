def main():
  x = get_int()
  print(f'x is {x}')

def get_int():
  while True:
    try:
      x = int(input("What's x?\n"))
    except ValueError:
      print("x should be an integer")
    else:
      break # breaking the loop when the input is valid or True for the progeam
  return x
main()