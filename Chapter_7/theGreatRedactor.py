#! python3
""" Searches for sensitive information and replaces it with redacted text """

import re
import sys

def main(): # main program loop

regexDict = {
    "ssn":      re.compile(r"^(\d{3})-(\d{2})-(\d{4})$"),    # social security number
    "dob":      re.compile(r"""^(
                        (0*?[1-9])|1[012])              # month
                        ([- / .])                       # separator
                        (0*?[1-9]|[12][0-9]|3[01])      # day    
                        \2                              # separator
                        (\d{2}|\d{4})                   # year
    )""", re.VERBOSE),
    "address":  re.compile
}

text = ""


if __name__ == "__main__":
    main()