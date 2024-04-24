"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox"."""

import random
import sys
import textwrap


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
                day = dayOfYear - days
                birthdays.append(f"{dictMonth} {day}")
                break
    return birthdays


def getMatch(birthdays):
    """Returns the birthday that occurs more than once in the list."""

    # Compare each birthday to every other birthday until match
    for a in range(0, len(birthdays)):
        for b in range(a + 1, len(birthdays)):
            if birthdays[a] == birthdays[b]:
                return birthdays[a]  # Return the matching birthday.


# Display the intro:
print("Birthday Paradox (barebones version)")
print("By Al Sweigart al@inventwithpython.com")
print()
print("How many birthdays shall I generate? (Max 100)")

while True:
    response = input("> ")
    if response.lower() == "q":
        print("exiting...")
        sys.exit()
    try:
        numBDays = int(response)
        break
    except ValueError:
        print("Error: You must enter an integer or 'q' to exit.")

if not (0 < numBDays <= 100):
    print("That is larger than 100.")
    sys.exit()

# Generate and display the birthdays:
print(f"\nHere are {numBDays} birthdays:")
birthdays = getBirthdays(numBDays)
print(", ".join(birthdays))
print()

# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Display the results:
print("In this simulation, ")
if match is not None:
    print(f"multiple people have a birthday on {match}.")
else:
    print("there are no matching birthdays.\n")
print()


# Run through 100,000 simulations:
print(f"Generating {numBDays} simulations 100,000 times...")
input("Press enter to continue...")
print("Running 100,000 simulations. Please wait...")

simMatch = 0  # How many simulations had matching birtdays in them.
for i in range(100_000):
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch += 1
print("\nDone.\n")
# Display simulation results:
probability = round(simMatch / 1000, 2)
message = f"Out of 100,000 simulations of {numBDays} people, there was a matching "
message += f"birthday in that group {simMatch} times. This means that {numBDays} people"
message += f" have a {probability}% chance of having a matching birthday in their "
message += "group. That is probably more than you would think!"

message = textwrap.wrap(message)

for i in range(len(message)):
    print(message[i])
