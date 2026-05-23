'''
Create a number guessing game where the computer tries to guess a secret number you set. 
The computer will generate random guesses within a range (1 to 10) and continue guessing until it finds 
the correct number.
'''
import random

secret_number = random.randint(1, 10)

guess = 0

while (guess != secret_number):
    guess = random.randint(1, 10)
    print("Guessing:",guess)

print("I guessed the right number! It was",secret_number)