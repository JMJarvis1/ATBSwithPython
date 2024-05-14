"""Basic ordring system for a sandwich shop."""
import pyinputplus as pyip


def main():
    """Main loop of the program"""

    MENU = {
        "bread": ["wheat", "white", "sourdough"],
        "protein": ["chicken", "turkey", "ham", "tofu"],
        "cheese": ["cheddar", "Swiss", "mozzarella"],
        "toppings": ["cheese", "mayo", "mustard", "lettuce", "tomato"],
    }

    CHOICES = {
        "bread": "",
        "protein": "",
        "cheese": "",
        "toppings": {k: False for k in MENU["toppings"]},
    }

    BASE_PRICE = 4.00

    sandwiches = []

    print("Welcome to Good Sandwich Place.\n")  # Greeting

    getOrder(MENU, CHOICES, sandwiches)  # Get cusomer order, validate input

    sandwichPrices = getPrices(sandwiches, BASE_PRICE)

    print(displayOrder(sandwiches, sandwichPrices))  # Display full order details


def getOrder(menu, choices, sandwiches):
    """Get and validate number of sandwiches to make.
        Build orders for eacch sandwich in order.
    Args:
        menu (dict): Containing sandwich options
        choices (dict): holds user menu selections for one sandwich
        sandwiches (list): holds all sandwiches in order
    """
    numSandwiches = pyip.inputNum(
        "How many sandwiches do you want to order today?\n", min=1, max=20
    )

    for i in range(numSandwiches):
        sandwich = buildSandwich(menu, choices.copy(), i + 1)
        sandwiches.append(sandwich)


def buildSandwich(menu, choices, sandwich):
    """Get sandwich selections from customer, validate inputs.

    Args:
        menu (dict): Containing sandwich options
        choices (dict): (copy) holds user menu selections for one sandwich
        sandwiches (list): holds all sandwiches in order

    Returns:
        dict: holds user menu selections for one sandwich
    """
    print("Sandwich %s: Please select from the following items...\n" % sandwich)

    for item, options in menu.items():
        match item:
            case "bread" | "protein":
                choices[item] = getBreadAndProtein(item, options)
            case "toppings":
                getToppings(menu, choices)
    return choices


def getBreadAndProtein(menuItem, itemOptions):
    """Get customer selection for bread and protein.

    Args:
        menuItem (str): Item's key/name from menu dict
        itemOptions (list): list of options from item's value in munu dict

    Returns:
        str: user selected option from itemOptions
    """
    prompt = "What is your choice of %s?\n" % menuItem
    return pyip.inputMenu(itemOptions, prompt=prompt, numbered=True)


def getToppings(menu, choices):
    """Get the user's selection for toppings and validates input.

    Args:
        menu (dict): Containing sandwich options
        choices (dict): FROM COPY; holds user menu selections for one sandwich
    """
    for topping in menu["toppings"]:
        choices["toppings"][topping] = getToppingChoices(topping)
        if topping == "cheese" and choices["toppings"]["cheese"] not in ("no", "n"):
            cheesePrompt = "What is your choice for cheese?\n"
            choices["cheese"] = pyip.inputMenu(
                menu["cheese"], prompt=cheesePrompt, numbered=True
            )


def getToppingChoices(topping):
    """Get and validate user slection of non-cheese toppings.

    Args:
        topping (str): key from menu["toppings"] dict (ex. "mayo")

    Returns:
        str: Yes/No response for topping
    """
    prompt = "Would you like %s on that? (Yes/No)\n" % topping
    return pyip.inputYesNo(prompt)


def getPrices(sandwiches, basePrice):
    """Get the price of each sandwich ordered.

    Args:
        sandwiches (list): list detailing the sandiches in the order
        basePrice (_type_): base price of a sandwich

    Returns:
        list: The tallied price of each sandwich ordered
    """
    sandwichPrices = []

    for sandwich in sandwiches:
        sandwichPrices.append((getSandwichPrice(sandwich, basePrice)))

    return sandwichPrices


def getSandwichPrice(sandwich, basePrice):
    """Tallies the price of each sandwich in the order

    Args:
        sandwich (dict): Contains all the sandwich options
        basePrice (int): the base price of a sandwich

    Returns:
        int: the tallied price of the sandwich
    """
    price = basePrice

    for option in sandwich.values():
        if isinstance(option, dict):
            for key, value in option.items():
                if value == "yes":
                    option = key
                    price = matchOptions(price, option)
        else:
            price = matchOptions(price, option)
    return price


def matchOptions(price, option):
    """Match indiviual options to respective cost increase,
    and increase price accordingly

    Args:
        option: option for price matching
        price (int): the current price of the sandwich

    Returns:
        int: the adjusted price of the sandwich based on option cost

    """
    match option:
        case "chicken" | "turkey" | "cheese" | "mayo":
            price += 0.50
        case "ham":
            price += 1.00
        case "sourdough" | "tofu":
            price += 1.50
        case _:
            price += 0.00
    return price


def displayOrder(sandwiches, sandwichPrices):
    """Display full order, neatly fromatted.

    Args:
        sandwiches (list): The sandiches in the order
        sandwichPrices (list): The respective pric of each sandwich in sandwiches

    Returns:
        str: the message to be displayed on the screen
    """
    message = ""
    subTotal = 0.00
    for index, sandwich in enumerate(sandwiches):
        subTotal += sandwichPrices[index]
        sandwich = sandwiches[index]
        sandwich["cheese"] = (
            f"with {sandwich['cheese']}"
            if sandwich["cheese"] != ""
            else "without cheese"
        )

        includedToppings = getIncludedToppings(sandwich)

        message += f"\nSandwich {index+1}: ${sandwichPrices[index]:.2f}\n"
        message += f"{'-'*4}{sandwich['protein'].title()} "
        message += f"{sandwich['cheese']} on {sandwich['bread']}"

        message = formatToppings(message, includedToppings) + ".\n"

    tax = 0.06 * subTotal
    message += f"\nSubtotal: {subTotal:.2f}"
    message += f"\nTax @6%:  {tax:.2f}"
    message += f"\nTotal:    {(subTotal + tax):.2f}\n"

    return message


def getIncludedToppings(sandwich):
    """Create list of toppings in sandwich

    Args:
        sandwich (dict): options selected for a single sandwich

    Returns:
        list: toppings for the sandwich
    """
    toppings = list(
        map(lambda x: x[0] if x[1] == "yes" else None, sandwich["toppings"].items())
    )
    return [x for x in toppings if x not in (None, "cheese")]


def formatToppings(message, includedToppings):
    """Format the topping strings based on type and location in message

    Args:
        message (str): message to display, detailing order
        includedToppings (list): topping ordered for a particular sandwich

    Returns:
        str: formatted message now including topping info
    """
    for index, topping in enumerate(includedToppings):
        if len(includedToppings) == 1:
            message += f" with {topping}"
        elif len(includedToppings) > 1:
            if topping == includedToppings[-1]:
                message += f" and {topping}"
            else:
                match index:
                    case 0:
                        message += f" plus {topping},"
                    case _:
                        message += f" {topping},"
    return message


if __name__ == "__main__":
    main()
