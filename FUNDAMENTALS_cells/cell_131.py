import csv

students = []

# Open the file and parse rows
with open('home.csv') as file:
    # skipinitialspace=True automatically cleans up any accidental spaces after commas
    reader = csv.DictReader(file, skipinitialspace=True)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

# Sort and print using the double quote fix for the f-string
for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} is from {student['home']}")