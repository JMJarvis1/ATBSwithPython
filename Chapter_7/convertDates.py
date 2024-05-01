#! python3
# convertDates.py - Convert a vareity of different formats to a single, standard format

import re


# TODO build regex fo date recognition

datePatterns = {
    "m/d/y": "^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[012])[-/.]((19|20)\d{2})$",
    "d/m/y": "", 
    "yyyy/mm/dd": "^(19|20)\d{2}[/ -. ](0[1-9]|1[012])[/ -. ](0[1-9]|[12][1-9]|3[01])$",

}

# TODO convert dates to 00/00/0000 format



