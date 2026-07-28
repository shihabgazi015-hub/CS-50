students = [
    "Shihab",
    "Abdullah",
    "Jabir",
    "Jabed"
]

for i in range(len(students)):
  name = students[i]
  print(name, end = " - ")
  match name:
    case "Shihab" | "Jabir":
      print("Shah Paran Hall")
    case "Abdullah":
      print("Dhamali Para")
    case "Jabed":
      print("Borogul")
    case _ : # for anyone who is not in our list
      print("Who?")


print(students)