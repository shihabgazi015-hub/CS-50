import csv

# with open('students.csv', encoding='utf-8') as file:
#     for line in file:
#         # row = line.strip().split(',')
#         name, house = line.strip().split(',')
#         print(f'{name} is in {house}')

# students = []

name = input("Name: ")
house = input("House: ")

with open('students.csv', "a", encoding='utf-8') as file:
    
    # reader = csv.reader(file)
    # for name, house in reader:
    #     students.append({'name': name, 'house': house})
    
    # writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames=['name', 'house'])
    # writer.writerow([name, house])
    writer.writerow({'name': name, 'house': house})
    
    # for line in file:
    #     name, house = line.rstrip().split(',')
#         students.append(f'{name} is in {house}')

# for student in sorted(students):
#     print(student)
        # student = {}
        # student['name'] = name
        # student['house'] = house
        
        
        
        # student = {'name': name, 'house': house}
        # students.append(student)

# def get_name(student):
#     return student['name']

# for student in sorted(students, key = lambda student: student['name']):#key=get_name, reverse=True):
#     print(f'{student['name']} is in {student['house']}')

# print(students) 