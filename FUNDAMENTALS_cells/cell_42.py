# for name in students & i in range(len(students)):
#   print(str(i + 1) + ".", name)

#  & is a bitwise operator in Python, not a tool for running dual loops

students = ["Shihab", "Abdullah", "Jabir", "Jabed"]

# start=1 tells Python to start counting at 1 instead of 0
for i, name in enumerate(students, start=1):
    print(f"{i}. {name}")