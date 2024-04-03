"""Comma, comma, comma, comma chameleon..."""

spam = ["apples", "bananas", "tofu", "cats"]


def printSpam(spam):
    """The spam list, served neat."""
    message = ""
    for item in spam:
        if item != spam[-1]:
            message += f"{item}, "
        else:
            message += f"and {item}."
    print(message.capitalize())


if __name__ == "__main__":
    printSpam(spam)
