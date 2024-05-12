import pyinputplus as pyip

while True:
    prompt = "Want to know how to keep an idiot busy fo hours?\n"
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break  
    else:
        print("'%s' is not a valid yes/no response." % response)
        continue

print("Thank you. Have a nice day.")