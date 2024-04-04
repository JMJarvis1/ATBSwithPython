catNames = []

while True:
    message = f"Enter the name of cat {str(len(catNames) + 1)}"
    message += " (Or enter nothing to stop.): "
    name = input(message)

    if name == "":
        break
    catNames = catNames + [name]  # list concatenation

print("The cat name are: ")
for name in catNames:
    print("  " + name)
