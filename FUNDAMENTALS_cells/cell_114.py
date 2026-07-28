students = []

with open("sample_data/california_housing_test.csv") as file:
  # Skip the header row (longitude, latitude, etc.) so it doesn't cause errors
  header = next(file)

  for line in file:
    row = line.rstrip().split(',')

    # Extract specific column indexes (0 for longitude, 1 for latitude)
    lng = row[0]
    lat = row[1]

    student = {}
    student["longitude"] = lng
    student["latitude"] = lat
    students.append(student)

# Print out a slice of the data so your screen doesn't fill up with 3000 rows
for student in students[:5]:
  print(f"Location is at Long: {student['longitude']}, Lat: {student['latitude']}")