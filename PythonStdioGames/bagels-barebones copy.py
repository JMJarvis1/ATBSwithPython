"""Bagels (barebones version), by Al Swweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues."""

import random


def main():
    print("""
    Bagels (barebones version), a deductive logic game.
    By Al Sweigart al@iinventwithpython.com

    When I say:     That means:
        Pico        One digit is correct but in the wrong place.
        Fermi       One digit is correct and in the right place.
        Bagels      No digit is correct.

    For example, if the number is 248 and you guess 843
    the clues would be Fermi Pico.
    """)

    # Make the secret number the player needs to guess:
    numbers = [num for num in range(10)]  # Create list of numbers 0-9
    random.shuffle(numbers)  # Randomly arrange list of numbers

    # Get first 3 numbers from list for secret number
    secretNum = str(numbers[0]) + str(numbers[1]) + str(numbers[2])

    print("""
    I have thought of a secret number.
    You have ten guesses to get it.
    """)

    numGuesses = 1

    while numGuesses <= 10:
        print(f"Guess #{numGuesses}")
        guess = input("> ")

        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1

        if guess == secretNum:
            break  # Victory condition, end loop
        elif numGuesses > 10:
            print("You are out of guesses.")
            print(f"The secret number was {secretNum}" "")

    print("Thanks for playing!")


def getClues(guess, secretNum):
    """Returns a string with Pico, Fermi, Bagel or win if number is
    guessed correctly"""
    if guess == secretNum:
        return "You guessed correctly!"

    clues = ""
    for i in range(3):
        if guess[i] == secretNum[i]:
            clues += "Fermi "  # A correct digit is in its correct place
        elif guess[i] in secretNum:
            clues += "Pico "  # A correct digit is not in its correct place

    if len(clues) == 0:
        return "Bagels"  # There are no correct digits
    else:
        # Make a single string from a list of string clues.
        return clues


# Call the main() function to play the game:
if __name__ == "__main__":
    main()
