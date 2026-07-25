# x = int(input("What's x?\t"))

# if x % 2 == 0:
#     print("Even")
# elif x % 2 != 0:
#     print("Odd")
# else:
#     print('Enter only real numbers')


# on a def
def main():
    x = int(input("What's x?\n"))
    if is_even(x):
        print('Even')
    else:
        print('Odd')

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# # shorcut
# def is_even(n):
#     return True if n % 2 == 0 else False
    
# more shorcut
def is_even(n):
    return (n % 2 == 0)
main()