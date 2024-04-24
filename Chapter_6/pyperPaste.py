"""Must be run locally to avoid error; Requires GUI, codespaces has no GUI"""

import os

userText = input("Enter text to be copied: ")


message = f"""
    
    Printing copied text....
    
    {os.system("echo '{}' | xsel -selection clipboard".format(userText))}


"""
print(message)
