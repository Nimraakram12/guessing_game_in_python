# Project 2: GUESS THE NUMBER GAME BY COMPUTER
# 1 to 100 number guessing game
#The computer will generate a random number between 1 to 100
#The user has to guess the number


import random

def guess_the_number():
    """Project 2: Guess The Number Game By Computer"""
    number = random.randint(1, 100)
    guesses_left = 7
    
    print("Welcome to Guess The Number Game By Computer")
    print("I am thinking of a number between 1 and 100")

    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the number in {7 - (guesses_left - 1)} tries!")
            return
            
        guesses_left -= 1

    print(f"\nYou've used all guesses. The number was {number}.")

# Call the function OUTSIDE of its definition
guess_the_number()