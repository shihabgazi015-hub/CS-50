def main():
    num = get_num()
    meow(num)

def get_num():
    while True:
        n = int(input('What\'s n?\n'))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print('meow')

main()