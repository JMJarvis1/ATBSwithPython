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
    numbers = list("0123456789")  # Create a list of digits (0 - 9)
    random.shuffle(numbers)  # Shuffle them into a random order

    # Get the first three digits in the list for the secret number
    secretNum = str(numbers[0]) + str(numbers[1] + str(numbers[2]))


if __name__ == "__main__":
    main()
