students = []

# 1. Initialize the empty list before the loop
students = []

with open("sample_data/california_housing_test.csv") as file:
    header = next(file)

    for line in file:
        row = line.rstrip().split(',')

        lng = row[0]
        lat = row[1]

        student = {"longitude" : lng, "latitude": lat}
        students.append(student)

# 2. Fix dictionary lookups using square brackets and string keys
def get_lat(student):
    return float(student["latitude"])

def get_lon(student):
    return float(student["longitude"])

# 3. Slice AFTER sorting to get the true top 5 highest longitudes
# (Slicing before sorting only sorts the first 5 arbitrary rows)
for student in sorted(students, key = get_lon, reverse = True)[:5]:
    print(f"Location is at Long: {student['longitude']}, Lat: {student['latitude']}")
