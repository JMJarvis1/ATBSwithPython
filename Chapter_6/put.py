from curses.ascii import isalnum


while True:
    age = input("Enter your age:\n")
    if age.isdecimal():
        break
    print("Please enter a number for your age.")

while True:
    password = input("Select a new password (letters and numbers only):\n")
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")
