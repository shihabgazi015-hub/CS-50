score = int(input("Score: "))

# Bangladeshi grade system
if score >= 80 and score <= 100:
    print("Grade: A+")
elif score >= 75 and score < 80:
    print("Grade: A")
elif score >= 70 and score < 75:
    print("Grade: A-")
elif score >= 65 and score < 70:
    print("Grade: B+")
elif score >= 60 and score < 65:
    print("Grade: B")
elif score >= 55 and score < 60:
    print("Grade: B-")
elif score >= 50 and score < 55:
    print("Grade: C+")
elif score >= 45 and score < 50:
    print("Grade: C")
elif score >= 40 and score < 45:
    print("Grade: C-")
elif score >= 0 and score < 40:
    print("Grade : F")
else:
    print("Please enter a valid number")

if score >= 80 and score <= 100:
    print("Grade: A+")
elif score >= 75:
    print("Grade: A")
elif score >= 70:
    print("Grade: A-")
elif score >= 65:
    print("Grade: B+")
elif score >= 60:
    print("Grade: B")
elif score >= 55:
    print("Grade: B-")
elif score >= 50:
    print("Grade: C+")
elif score >= 45:
    print("Grade: C")
elif score >= 40:
    print("Grade: C-")
elif score >= 0:
    print("Grade : F")
else:
    print("Please enter a valid number")