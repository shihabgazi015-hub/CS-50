with open("names.csv") as file:
  for line in file:
    # Fixed: split(",") explicitly cuts the row at the comma character
    row = line.rstrip().split(",")

    # row[0] is now the full name, row[1] is the home town
    name = row[0].strip()
    city = row[1].strip()

    print(f"{name} is in {city}")
