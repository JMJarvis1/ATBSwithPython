#! python3
""" Strips the designated character from each end of a given string. """

import re

def main():
    
    try:
        text = input("Enter text: ")
        character = input("Enter the character you wished stripped from the text: ")
    except KeyboardInterrupt:
        text = "Hello, world "
        character = " "
   

    print()
    print(stripEnds(text, character))
  
def stripEnds(text, character=" "):
    """Strips a designated character from each end of a string. 

    Args:
        text (str): The sting to be transformed
        character (str, optional): The character to be stripped. Defaults to " ".

    Returns:
        str: A string stripped of the the designated character, or the original text
        if the operation cannot be completed. 
    """
    regex = re.compile(fr"(?<={character})\S+(?={character})")
    mo = regex.search(text)
    try:
        newText = mo.group()
        return newText
    except AttributeError:
        return text
    




if __name__ == "__main__":
    main()