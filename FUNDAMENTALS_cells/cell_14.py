# Ask user for their name
name = input("Whats your name?\n").strip().title()

first, last = name.split(" ")
# Say, salam to first name
print(f'Assalamualaikum, {first}')