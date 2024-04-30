#! python3
# convertDates.py - Convert a vareity of different formats to a single, standard format

import re


# TODO build regex fo date recognition

datePattern = re.compile(r"""
    ([a-zA-z]{3,9}(\.)?|\d{4})    # first segment   
    ((-|\/|(\.)?\s)*              # separator
    ([0-9]{1,2}[stnd.]*)          # Day or Month
    ((-|\/|[\.,])(\s)?)           # separator
    (([a-zA-z]{3,9}(\.)?)?        # month name (Apr./April)
    ([0-3]{,1}[0-9])?             # month numeric
    (\d{4}|)?)$                   # year numeric   
""") 

# TODO convert dates to 00/00/0000 format



