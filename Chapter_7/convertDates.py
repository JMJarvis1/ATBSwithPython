#! python3
# convertDates.py - Convert a vareity of different formats to a single, standard format

import re


# TODO build regex fo date recognition

# TODO convert dates to 00/00/0000 format

datePattern = re.compile(r"""
    ([0]*[1-12]|\d{4}|)

""")



