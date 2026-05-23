import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

while True:
    user_choice = int(input("Enter\n 1. for rock\n 2. for paper\n 3. for scissor\n\n ---> "))
    if (user_choice == 1 or user_choice == 2 or user_choice == 3):
        break

computer_choice = int(random.choice("123"))

print(f"Your choice = {RPS(user_choice).name}")
print(f"Computer chose = {RPS(computer_choice).name}")

if user_choice == 1 and computer_choice == 3:
    print("You win!! 🥳🙌")
elif user_choice == 2 and computer_choice == 1:
    print("You win!! 🥳🙌")
elif user_choice == 3 and computer_choice == 2:
    print("You win!! 🥳🙌")
elif user_choice == computer_choice:
    print("Game Tied. 😮")
else:
    print("Python wins. 🐍")
