name = input('What\'s your name?\n').capitalize()

match name:
    case 'Harry' | 'Hermoine' | 'Ron':
        print('Gryffindor')
    # case 'Hermoine':
    #     print('Gryffindor')
    # case 'Ron':
    #     print('Gryffindor')
    case 'Draco':
        print('Stytherin')
    case _: # '_' works for any case
        print('Who?')