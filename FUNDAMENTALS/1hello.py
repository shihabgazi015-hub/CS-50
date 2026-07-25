''' print("Hello")
# print("Assalamualaikum")'''

# 1. Take input from the user
name = input("What is your name? \n").capitalize()
#using capitalize() to make the first letter uppercase and rest lowercase
# 2. Greet the user with their name
print("Salam,", end= " ")
print(name, end = "!\n")

print(f"Salam \"{name}\"")

name = name.strip().title() #capitalize won't work
print(f"Salam \"{name}\"")

