students = [
    {'name': 'Shafi', 'house': 'Dhaka', 'partronus': 'Chandpur'},
    {'name': 'Ali', 'house': None, 'partronus': None},
    {'name': 'Radia', 'house': "Cox's Bazar", 'partronus': 'Cumilla'},
    {'name': 'Shihab', 'house': 'Sylhet', 'partronus': 'Cumilla'}
]

print(students)

for student in students:
    print(student["name"], student['house'], student['partronus'], sep = ', ')