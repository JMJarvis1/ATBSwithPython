#! python3 
# bulletPointAdder.py - Adds Wikipedia buller points to the start
# of each line of text on the clipboard.

import pyperclip

# TODO: Use pyperclip locally to complete project
text = "Lists of animals\nLists of aquarium lif\nLists of biologists by author abbreviation\nList of cultivars" #pyperclip.paste()


lines = text.split('\n')

for i in range(len(lines)): # Loop through all indexes in the 'lines' list
    lines[i] = f"*{lines[i]}"
    
text = '\n'.join(lines)

print(text)

#pyperclip.copy(text)