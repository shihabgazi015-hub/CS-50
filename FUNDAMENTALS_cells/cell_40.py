def main():
  number = get_number()
  meaun(number)

def get_number(m = 3):
  while True:
      m = int(input("What's m?"))
      if m > 0:
        break
  return m # write return m because without it, the function returns None by default, making it impossible to use the number you typed anywhere else in your program.

def meaun(m):
  for _ in range(m):
    print("Meaun")

main()