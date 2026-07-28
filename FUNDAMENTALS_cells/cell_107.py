with open('names.txt', 'r') as file:
  # r helps us to read
  lines = file.readlines()

for line in lines:
  print('Salam,', line)