students = []

with open('home.csv') as file:
  for line in file:
    name, home = line.strip().split()
    student = {'name' : name, 'home' : home}
    students.append(student)

for student in sorted(students, key = lambda student:student['name']):
  print(f'{student['name']} is from {student['home']}')