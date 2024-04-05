allGuests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"ham sandwiches": 3, "apples": 3},
    "Carol": {"cups": 3, "apple pies": 1},
}

items = []
message = "         Total items brought:\n"
message += "    " + ("-" * len(message)) + "\n"


def totalBrought(guests, item):
    numBrought = 0
    for key, value in guests.items():
        numBrought = numBrought + value.get(item, 0)
    return numBrought

    print("Number of things people brought:")


for value in allGuests.values():
    for k, v in value.items():
        if v > 0 and v not in items:
            items.append(k)


for item in items:
    longest = len(max(items, key=len))
    message += f"       - {item.capitalize()}"
    if len(item) != longest:
        padding = longest - len(item)
        message += f"{padding * ' '}"

    message += f"\t{totalBrought(allGuests, item)}\n"

print(message)
