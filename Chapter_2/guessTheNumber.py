# This is a guess the number game.
import random
import sys


def validateIntegerConversion(value:str) -> int:
    try: 
        return int(value)
    except ValueError:
        sys.exit()


def guessTheNumber():
    
    secretNumber = random.randint(1, 20)

    print("I'm thinking about a number between 1 and 20.")

    for guessesTaken in range(1, 7):
        guess = input("Make a guess.\n")
        guess = validateIntegerConversion(guess)
        if guess < secretNumber:
            print("Too low!")
        elif guess > secretNumber:
            print("Too high!")
        else:
            break # Correct guess.
     
    if guess == secretNumber:
        print(f"Good job! You guessed my number in {guessesTaken} guesses!")
    else:
        print(f"Nope. The number I was thinking of was {secretNumber}.")

if __name__ == "__main__":
    guessTheNumber()
    
