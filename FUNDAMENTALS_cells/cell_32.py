score = 85  # Example score

match score:
    case _ if 100 >= score >= 80: # _ acts as a capture variable, and the if applies the condition (guard)
        print("Grade 4.00")
    case _ if score >= 75:
        print("Grade 3.75")
    case _ if score >= 70:
        print("Grade 3.50")
    case _ if score >= 65:
        print("Grade 3.25")
    case _ if score >= 60:
        print("Grade 3.00")
    case _ if score >= 55:
        print("Grade 2.75")
    case _ if score >= 50:
        print("Grade 2.50")
    case _ if score >= 45:
        print("Grade 2.25")
    case _ if score >= 40:
        print("Grade 2.00")
    case _:  # The '_' acts as the 'else' wildcard for anything else
        print("Grade 0.00")
