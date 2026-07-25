from random import choice, randint

def repeat_func(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Enter a valid number!")

def on():
    repeat_var = repeat_func("How many times do you want to repeat?\n")

    true_count = 0
    false_count = 0

    for _ in range(repeat_var):
        coin = choice([True, False])
        print(coin)
        
        # count ratio
        if coin == True:
            true_count += 1
        else:
            false_count += 1

    # ratio print
    print("\n--- RESULT ---")
    print(f"True percentage  : {true_count/repeat_var*100:.2f}%")
    print(f"False percentage : {false_count/repeat_var*100:.2f}%")


    total = true_count + false_count
    print(f"\nRatio = True:{true_count}/{total}, False:{false_count}/{total}")

    number = randint(1, 10)
    print("Random number:", number)

on()
