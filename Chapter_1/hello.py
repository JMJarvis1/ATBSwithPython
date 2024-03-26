# This program says hello world and asks for my name

print("Hello, world!")
print("What is your name?")  # ask for their name

myName = input()

print("It is good to meet you, " + myName.capitalize())
print(f"The length of your name is: {len(myName)} letters")

myAge = input("What is your age? ")  # Ask for their age.

print(f"You will be {str(int(myAge) + 1)} in a year.")
