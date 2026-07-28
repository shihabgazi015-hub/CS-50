def calculate_e_limit(n=100000000):
    return (1 + 1 / n) ** n

print(calculate_e_limit())  # Output: 2.7182818148460567 (slight rounding error due to float limits)
