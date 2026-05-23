'''
simulating a dice roll until you get a 6.
'''

import random
sides = int(input("Enter the total sides of the roll: "))
roll = 0

while roll != sides:
    roll = random.randint(1, sides)
    print(f"You rolled {roll}")
