
import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers)

    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception(f'The digits mus add up to ten, not {sum(numbersList)}.')
    return int(numbers) # Return an int form of numbers

response = pyip.inputCustom(addsUpToTen) 
        




