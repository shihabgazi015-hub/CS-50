students = {
    'Shihab': 'Sylhet',
    'Radia': 'Cox\'sbazar',
    'Shafi': 'Dhaka'            
            }

print(students)
print(students['Radia'])
print(students['Shafi'])

for student in students:
    print(student, students[student], sep = ' -> ')