names = []

for i in range(3):
    names.append(input('Enter your name: '))
    # name =  input('Enter your name: ')
    # names.append(name)
    print(f'hello, {names[i]}')

for name in sorted(names):
    print(f'Hello, {name}')