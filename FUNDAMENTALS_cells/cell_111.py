names = [
    "Shihab",
"Muktadir Shihab",
"Muktadir Shihab Gazi",
"Ibn Hira"]

with open("names.txt", "w") as file:
  for name in names:
    file.write(f'{name}\n')