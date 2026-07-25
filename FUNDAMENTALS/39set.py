students = [
    {"name" : "Shihab1", "house" : "Sylhet word no 1"},
    {"name" : "Shihab2", "house" : "Sylhet word no 2"},
    {"name" : "Shihab3", "house" : "Sylhet word no 3"},
    {"name" : "Shihab4", "house" : "Sylhet word no 4"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)