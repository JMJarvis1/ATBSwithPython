myPets = ["Zophie", "Pooka", "Fat-tail"]
name = input("Enter a pet name: ")
if name not in myPets:
    print(f"I do not have a pet named {name}.")
else:
    print(f"{name} is my pet.")
