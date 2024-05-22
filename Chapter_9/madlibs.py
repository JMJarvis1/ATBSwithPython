#! Python3
#
# madlibs.py - Reads in text file and lets the user ad their own text anywhere
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
#
# Example: text: The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN
#                was unaffected by these events.
#          user: Adjective - silly
#                Noun      - chandelier
#                Verb      - screamed
#                Noun      - pickup truck
#          result: The silly panda walked to the chandelier and then screamed. A
#                  nearby pickup truck was unaffected by these events.

from pathlib import Path
import glob
import os
from pyclbr import Class
import random


def main():
    WORDLIST = (
        "ADJECTIVE",
        "NOUN",
        "VERB",
    )

    madPath = getProgramPath()
    madTextPath = os.path.join(madPath, "madlibs.txt")

    if "madlibs.txt" not in glob.glob(madPath):  # Create file with default text
        creatMadlibTextFile(madTextPath)

    with open(madTextPath, "r") as f:
        madList = f.readlines()
        madText = random.choice(madList)

    print(madText.ljust(79))


def getProgramPath():
    for r, d, f in os.walk(Path.cwd()):
        for file in f:
            if file == "madlibs.py":
                filePath = os.path.join(r, file)
                p = Path(filePath)
                madPath = str(p.parent.absolute())
    return madPath


def creatMadlibTextFile(filePath):
    defaultText = "The ADJECTIVE panda walked to the NOUN and then VERB. "
    defaultText += "A nearby NOUN was unaffected by these events."

    with open(filePath, "w") as f:
        f.write(defaultText)


if __name__ == "__main__":
    main()
