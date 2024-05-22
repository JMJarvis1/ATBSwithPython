#!Python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Useage: python3 mcb.pyw save <keyword> - Saves clipboard to keyword
#         python3 mcb.pyw <keyword> - Loads keyword to clipboard.
#         python3 mcb.pyw list - Loads all keywords to clipboard.
#         python3 mcb.pyw delete <keyword> - Deletes keyword from shelf file.
#         python3 mcb.pyw delete * - Deletes all entries in shelf file.

# TODO: #3 Test delete features

import shelve
import pyperclip
import sys

mcbShelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == "save" and sys.argv[2] != "*":
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == "delete":
        if sys.argv in mcbShelf:
            del mcbShelf[sys.argv[2]]
        elif sys.argv[2] == "*":
            mcbShelf.clear()
elif len(sys.argv) == 2:
    # TODO: List keywords and load content
    if sys.argv[1].lower() == "list":
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
