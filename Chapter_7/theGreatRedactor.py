#! python3
""" Searches for sensitive information and replaces it with redacted text """

from operator import sub
import re
import sys

def main(): # main program loop

    regexDict = {
        "ssn":      re.compile(r"(\d{3})-(\d{2})-(\d{4})$"),    # social security num.
        "dob":      re.compile(r"""(
                    (0*?[1-9]|1[012])                           # month
                    ([- / .])+?                                 # separator
                    (0*?[1-9]|[12][0-9]|3[01])                  # day    
                    ([- / .])+?                                 # separator
                    (\d{2,4})                                   # year
            )""", re.VERBOSE),
        "address":  re.compile(r"""(
                    (\d{1,9}\s[\w .]*)\n                        # number & street
                    ([a-zA-Z .]*\w{1,5})?                       # apt./suite
                    ([^\d,]{1,40},\s)                           # city/town/locale
                    ([A-Z]{2}|[a-zA-Z .]*)[\n ]                 # state/territory
                    (\d{5}(-\d{4})?)                            # zipcode
            )""", re.VERBOSE),
        "phone" : re.compile(r"""(
                    (\+?(\d{1,3}(-\d{1,4})*))?                  # coutry code
                    ([. -]?)                                    # separator
                    (\(?(\d{3})\)?)                             # area code 
                    ([. -])?                                    # separator
                    (\d{3})([. -])?(\d{4})                      # xxx-xxxx
                    (\s[EXT:extension.]{1,9}\s?\d{1,4})?        # extension
            )""", re.VERBOSE)
    }

    # 
    
    text = """
       Name: John Jarvis
      Phone: +1 (734) 255-6699
    Address: 21562 Homer St.
             Dearborn, MI 48124-2911
        DOB: 11/04/1980
        SSN: 123-45-6789
"""
    print(text)

    redacted = matchObjects(regexDict, text)
    
    print(redacted)

def matchObjects(regexDict, text):
    redacted = text
    substitutions = {
        "ssn": "***-**-****",
        "dob": "**/**/****",
        "address": "***********",
        "phone": "(***) ***-****",
    }
    for key, regex in regexDict.items():
        redacted = regex.sub(substitutions[key], redacted,)
    return redacted            






if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()