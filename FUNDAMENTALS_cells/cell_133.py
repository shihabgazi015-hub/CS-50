import csv

# Get data from the user
name = input("What's your name? ")
home = input("What's your home? ")

# Open the file in append mode with newline safety
with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    # Fixed the typo from 'hame' to 'home'
    writer.writerow([name, home])
