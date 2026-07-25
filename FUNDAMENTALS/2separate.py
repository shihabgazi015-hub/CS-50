# Ask user for thyeir name
name = input("What's your name?\n").strip().title()

# Separating the name into first and last part
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")