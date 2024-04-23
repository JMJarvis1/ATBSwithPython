"""Must be run locally to avoid error; Requires GUI, codespaces has no GUI"""

import pyperclip

userText = input("Enter text to be copied: ")

copyText = pyperclip.copy(userText)

message = f"""
    
    Printing copied text....
    
    {pyperclip.paste(copyText).rjust(30)}

"""
print(message)
