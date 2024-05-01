#! python3
#  convertDates.py - Convert a vareity of different date formats to a single,
#  standard format

import re
import sys
from tokenize import group

def main():
    # TODO build regex fo date recognition

    datePatterns = ["mmddyyyy","yyyymmdd",]
    

    dateRegex = {pattern:getDateRegexPatterns(pattern) for pattern in datePatterns}
    matches = []
    
    
    


    # TODO convert dates to 00/00/0000 format
    text = """
            My birthdate is 11/04/1980 dksl;fkhjas]]]ppsdmfps4123442424 Tomorrw 
            is 02.05.2024 and this year3022 wil20 end on 2023-12-31. 
        """
    
    for pattern, regex in dateRegex.items():
        for groups in regex.findall(text):
            if pattern.endswith('y'):
                date = '/'.join([groups[1], groups[3], groups[5]])
            elif pattern.startswith('y'):
                date = '/'.join([groups[4], groups[6], groups[1]])
            matches.append(date) 
            
            

    for date in matches:
        print(date)


def getDateRegexPatterns(pattern):
    
    match pattern:
        case 'mmddyyyy':
            return re.compile(r"""(
                (0[1-9]|1[012])             # month
                ([- / .])                   # separator
                (0[1-9]|[1,2][0-9]|3[01])   # day
                ([- / .])                   # repeat separator
                ((19|20)\d{2})              # year      
                )""", re.VERBOSE)
        case 'yyyymmdd':
            return re.compile(r"""(
                ((19|20)\d{2})              # year      
                ([- / .])                   # separator
                (0[1-9]|1[012])             # month
                ([- / .])                   # repeat separator
                (0[1-9]|[1,2][0-9]|3[01])   # day
                )""", re.VERBOSE)
            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()