birthdays = {
    "Alice": "Apr 1",
    "Bob": "Dec 12",
    "Carol": "Mar 4",
}

while True:
    name = input("Enter a name (blank to quit)\n")
    if name == "":
        break
    if name.capitalize() in birthdays:
        print(f"{birthdays[name.capitalize()]} is the birthday of {name}.")

    else:
        print(f"I do not have birthday information for {name.capitalize()}.")
        birthdays[name.capitalize()] = input("What is their birthday?\n").capitalize()
        print("Birthday database updated.")
