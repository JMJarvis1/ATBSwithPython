#! python3
# bulletPointAdder.py - Adds Wikipedia buller points to the start
# of each line of text on the clipboard.

import pyperclip

# TODO: Use pyperclip locally to complete project
text = pyperclip.paste()


lines = text.split("\n")

for i in range(len(lines)):  # Loop through all indexes in the 'lines' list
    lines[i] = f"* {lines[i]}"

text = "\n".join(lines)

pyperclip.copy(text)
