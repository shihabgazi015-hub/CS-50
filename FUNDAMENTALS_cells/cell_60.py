import random

# 1. Roll a random dice number between 1 and 6
dice_roll = random.randint(1, 6)
print(f"Rolled: {dice_roll}")

# 2. Pick a random winner from a list
players = ["Shihab", "Abdullah", "Jabir", "Jabed"]
winner = random.choice(players)
print(f"The lucky winner is: {winner}")