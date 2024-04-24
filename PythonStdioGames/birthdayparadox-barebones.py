"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox"."""

import random
import sys


def getBirthdays(numberOfBirthdays):
    """Returns a list of birthday dates."""
    birthdays = []

    for i in range(numberOfBirthdays):
        dayOfYear = random.randint(1, 365)

        dateDict = {
            "Dec": 334,
            "Nov": 304,
            "Oct": 273,
            "Sep": 243,
            "Aug": 212,
            "Jul": 181,
            "Jun": 151,
            "May": 120,
            "Apr": 90,
            "Mar": 59,
            "Feb": 31,
            "Jan": 0,
        }
        for dictMonth, days in dateDict.items():
            if dayOfYear > days:
                month = dictMonth
                day = dayOfYear - days
                birthdays.append(f"{month} {day}")
                break
    return birthdays


def getMatch(birthdays):
    """Returns the birthday that occurs more than once in the list."""

    # Compare each birthday to every other birthday.
    for a in range(0, len(birthdays)):
        for b in range(a + 1, len(birthdays)):
            if birthdays[a] == birthdays[b]:
                return birthdays[a]  # Return the matching birthday


# Display the intro:
print("Birthday Paradox (barebones version)")
print("By Al Sweigart al@inventwithpython.com")
print()
print("How many birthdays shall I generate? (Max 100)")

response = input("> ")

if not (0 < int(response) <= 100):
    print("That is larger than 100.")
    sys.exit()

numBDays = int(response)

# Generate and display the birthdays:
print()
print(f"Here are {numBDays} birthdays:")
birthdays = getBirthdays(numBDays)
print(", ".join(birthdays))
print()

# Determine if there are two birthdays that match
match = getMatch(birthdays)

print("In this one simulation, ", end="")
if match is not None:
    print(f"Multiple people have birthdays on {match}")
else:
    print("There are no matching birthdays.")
print()

# Run through 100,000 simulations:
print(f"Generating {numBDays} random birthdays 100,000 times...")
input("Press enter to begin...")

print("Running 100,000 simulations. Please wait...")
simMatch = 0  # How many simulations had matching birtdays in them.
for i in range(100_000):
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch += 1
print("Done.")

# Display simulation results:
probability = round(simMatch / 1000, 2)
print(f"Out of 100,000 simulations of {numBDays} people, there was a")
print(f"matching birthday in that group {simMatch} times. This means")
print(f"that {numBDays} people have a {probability}% chance of")
print("having a matching birthday in their group.")
print("That is probably more than you would think!")
