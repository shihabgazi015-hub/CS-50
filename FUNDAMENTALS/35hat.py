import random

class Hat:
    # def __init__(self):
    #     self.houses = ["Shah Paran", "Mujtaba", "Bijoy 24"]
    #     self.names = ["Shihab1", "Radia", "Ali", "Shohan", "Rashed", "Rafsan"]
        
    houses = ["Shah Paran", "Mujtaba", "Bijoy 24"]
    # def sort(self, name):
    #     print(random.choice(self.names), 'is in', random.choice(self.houses))
    @classmethod
    def sort(cls, name):
        print(name, 'is in', random.choice(cls.houses))
    
# hat = Hat()

# i = input("How many times")
# for _ in range(int(i)):
#     hat.sort("Shihab")
Hat.sort("Shihab")