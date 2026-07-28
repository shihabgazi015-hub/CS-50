name = input("What's your name?\n")

file = open("names.txt", "a") # 'w' just writes the whole file while 'a' appends to the file
file.write(f'{name.title()}\n')
file.close()