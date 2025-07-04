import random

def guessing_game():
    number = random.randint(1, 100)
    guess = None

    print("WELCOME TO MY GAME")
    print("The Number is Between 1-100")
    print("Good Luck!")


    while guess != number:
        guess = int(input("GUESS: "))
        if guess < number:
            print("TOO LOW!")
        elif guess > number:
            print("TOO HIGH!")
        else:
            print(f"YOU'RE BRILLIANT IT WAS {number}!")

guessing_game()
