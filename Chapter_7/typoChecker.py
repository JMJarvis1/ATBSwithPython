#! python3
""" Checks texts for common typos. """

import re
import colorama


def main():
    
    # dict holding regex patterns for some common typos
    typoRegex = {
        "repeatWords": r"\b(\w+)\s+\1\b",                   # repeated repeated words
        "repeatPunctuation": r"[/(?!%:;\"])\1|(\.{2})\2",   # punctuation,, repeated 
        "extraSpace": r"\b( ){2,}",                         # too  many  spaces
    }

    text = ""      # Text to be examined
    
if __name__ == "__main__":
    main()