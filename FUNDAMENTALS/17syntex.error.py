try:
    x = int(input('What\'s x?\n'))
except ValueError:
    print('x is not an integer')
else:
    print(f'x is {x}')