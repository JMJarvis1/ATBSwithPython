# inventory.py

from operator import add


stuff = {
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12,
}

dragonLoot = ['gold coin', 'dagger', "gold coin", "ruby"]


def displayInventory(inventory: dict):
    """Displays inventory contents, neatly formatted.

    args:
        inventory (dict) -> key = item, value = count

    return: None

    """
    totalItemCount = 0

    message = "\nInventory:\n\n"

    for item, count in inventory.items():
        message += f"{count} {item}\n\n"
        totalItemCount += count

    message += f"Total number of items: {totalItemCount}\n"

    print(message)

def addToInventory(inventory: dict, addedItems:list):
    """ Adds items to inventory. """
    for newItem in addedItems:
        inventory[newItem] = 1 if newItem not in inventory else inventory[newItem] + 1
       

if __name__ == "__main__":
    displayInventory(stuff)
    addToInventory(stuff, dragonLoot)
    displayInventory(stuff)
