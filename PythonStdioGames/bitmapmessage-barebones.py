"""Bitmap message (barebones version)
by Al Sweigart al@inventwithpython.com
Display a text message according to the bitmap image provided."""

import sys
import textwrap

bitmap = """
        ********
     ********
   ********
  ********
   ********
     ********
        ********
       ********
     ********
********************
********************
***************************
*********************    **
*********************    **
*********************    **
**************************
********************
 ******************
"""
print("Bitmap message, by Al Sweigart al@inventwithpython.com")
print("Enter the message to display with the bitmap.")

message = input("> ")
if message == "":
    sys.exit()

# Loop over each line in the multiline bitmap:
for line in bitmap.splitlines():
    # Loop over each charachter in the line:
    for i in range(len(line)):
        if line[i] == " ":
            # Print an empty space since there is a space in the bitmap:
            print(" ", end="")
        else:
            # Print a character from the message:
            print(message[i % len(message)], end="")
    print()
