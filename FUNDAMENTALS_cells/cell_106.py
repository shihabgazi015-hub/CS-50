name = input("What's your name?\n")

with open('names.txt', 'a') as file:
  file.write(f'{name}\n')