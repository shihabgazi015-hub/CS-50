# A list of student tuples: (Name, Grade)
students = [("Anika", 92), ("Tanvir", 78), ("Zayan", 85)]

# Sort the students based on their grades (index 1 of the tuple)
students.sort(key=lambda student: student[1])

print(students)
# Output: [('Tanvir', 78), ('Zayan', 85), ('Anika', 92)]