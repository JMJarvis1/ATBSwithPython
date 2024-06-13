#! Python3 fileCreator.py -- create dummy files

import random
import os


def createFiles(folder):
    os.chdir(folder)
    choices = ["Hello, world!", "spam", "bacon", "eggs", "42"]
    for i in range(10):
        filename = "spam00" + str(random.randint(1, 15)) + ".txt"
        try:
            with open(filename, "x") as f:
                choice = random.choice(choices)
                f.write(choice)
        except FileExistsError:
            continue


if __name__ == "__main__":
    createFiles(
        "/Users/johnmichaeljarvis/Documents/GitHub/ATBSwithPython/Chapter_10/gapFIles"
    )
