def main():
  x = get_int("Wat's x? ")
  print(f'x is {x}')

def get_int(question_ans):
  while True:
    try:
      return int(input(question_ans))
    except ValueError:
      pass
main()