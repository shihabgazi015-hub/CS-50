# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)

# print(int(input("What's x? "))+int(input("What's y? ")))
# print(float(input("What's x? "))+float(input("What's y? ")))

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)

# print(z)
# print(f"{z:,}")

# z = 2 / 3
# print(round(z, 5)) # does the same thing
# print(f"{z:.2f}") # does the same thing

def main():
    x = int(input('what is x?'))
    print("x squared is", square(x))

def square(n):
    # return n*n
    # return n**2
    return pow(n, 2)

main()