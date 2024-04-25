"""Bouncing DVD logo (barebones version)
by Al Sweigart, al@inventwithpython.com
A bouncing DVD logo animation. Yo have to 'be of a certain age' to appreciate this.
Presss Ctrl-C to stop."""

import sys
import random
import time
import bext

WIDTH, HEIGHT = bext.size()
WIDTH -= 1  # Adjust for a Windows bug.

colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
directions = ["UR", "UL", "DR", "DL"]


def main():
    bext.clear()
    logo = {
        "color": random.choice(colors),
        "x": random.randint(1, WIDTH - 4),
        "y": random.randint(1, HEIGHT - 4),
        "dir": random.choice(directions),
    }

    if logo["x"] % 2 == 1:
        logo["x"] -= 1  # Make sure x is even so it can hit the corner

    while True:  # Main program looop.
        # Erase the logo's current location:
        bext.goto(logo["x"], logo["y"])
        print("   ", end="")  # (!) Try commenting this line out.

        originalDirection = logo["dir"]

        # See if the logo bounces off the corners:
        if logo["x"] == 0 and logo["y"] == 0:
            logo["dir"] = "DR"
        elif logo["x"] == 0 and logo["y"] == HEIGHT - 1:
            logo["dir"] = "UR"
        elif logo["x"] == HEIGHT - 3 and logo["y"] == 0:
            logo["dir"] = "DL"
        elif logo["x"] == HEIGHT - 3 and logo["y"] == HEIGHT - 1:
            logo["dir"] = "UL"

        # See if the logo bounces off of the left edge:
        elif logo["x"] == 0 and logo["dir"] == "UL":
            logo["dir"] = "UR"
        elif logo["x"] == 0 and logo["dir"] == "DL":
            logo["dir"] = "DR"

        # See if the logo bounces off of the right edge:
        # (WIDTH - 3) because DVD has three letters
        if logo["x"] == (WIDTH - 3) and logo["dir"] == "UR":
            logo["dir"] = "UL"
        elif logo["x"] == (WIDTH - 3) and logo["dir"] == "DR":
            logo["dir"] = "DL"

        # See if the logo bounces off of the top edge:
        # (HEIGHT - 1) because DVD is one line in heght
        if logo["y"] == 0 and logo["dir"] == "UR":
            logo["dir"] = "DR"
        elif logo["y"] == 0 and logo["dir"] == "UL":
            logo["dir"] = "DL"

        # See if the logo bounces off of the bottom edge:
        # (HEIGHT - 1) because DVD is one line in heght
        if logo["y"] == (HEIGHT - 1) and logo["dir"] == "DL":
            logo["dir"] = "UL"
        elif logo["y"] == (HEIGHT - 1) and logo["dir"] == "DR":
            logo["dir"] = "UR"

        if logo["dir"] != originalDirection:
            # Change the color when the logo bounces
            logo["color"] = random.choice(colors)

        # Move the logo. (X moves by two because the terminal characters are twice as
        # tall as they are wide.)
        if logo["dir"] == "UR":
            logo["x"] += 2
            logo["y"] -= 1
        elif logo["dir"] == "UL":
            logo["x"] -= 2
            logo["y"] -= 1
        elif logo["dir"] == "DR":
            logo["x"] += 2
            logo["y"] += 1
        elif logo["dir"] == "DL":
            logo["x"] -= 2
            logo["y"] += 1

        # Draw the logo at it's new location:
        bext.goto(logo["x"], logo["y"])
        bext.fg(logo["color"])
        print("DVD", end="")

        sys.stdout.flush()  # Required for bext using programs

        time.sleep(0.002)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
