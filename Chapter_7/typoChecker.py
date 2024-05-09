#! python3
""" Checks texts for common typos. """

import re
import colorama


def main():
    
    # dict holding regex patterns for some common typos
    typoRegex = {
        "repeatWords": r"\b(\w+)\s+\1\b",                   # repeated repeated words
        "repeatPunctuation": r"([/(?!%:;\"])\1|(\.{2})\2",   # punctuation,, repeated 
        "extraSpace": r"\b( ){2,}",                         # too  many  spaces
    }

    text = "manymany"                           # Text to be examined

    typoCheck(text, typoRegex)
    # print(text)
 

def typoCheck(text, typoRegex):
    typos = {k:[] for k in typoRegex.keys()}

    for typoType, regex in typoRegex.items():
        pattern = re.compile(regex)
        for typoKey, list in typos.items():
            if typoKey == typoType:
                text = pattern.sub("typo", text)

    # for key, groups in typos.items():
    #     print(groups)
    print(text)

if __name__ == "__main__":
    main()