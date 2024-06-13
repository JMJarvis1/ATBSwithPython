#! Python3 gapFiller.py - Searches a folder for instances where a set
#  numbered files has a gap in numbering. The program then renames
#  the last filename in the numbered sequence to fill the gap.


import os
import re
import sys


def gapFiller(folder):
    platform = sys.platform
    if platform in ["darwin", "linux"]:
        os.system("clear")
    elif platform == "win32":
        os.system("cls")
    else:
        print("Unknown operating system. Exiting...")
        os.system.exit()

    mo = re.compile(
        r"""
            ^\b             # Must start with word boiundary 
            ([A-Za-z]+)      # One or more letter characters     (0) 
            ([0]*)          # Any number of leading zeroes      (1)
            ([0-9]+)        # One or more numeric characters    (2)
            (\.)            # Separator                         (3)
            (\w{2,4})       # File extension                    (4)
            \b$             # Must end in word boundaary


""",
        re.VERBOSE,
    )
    source = os.path.abspath(folder)
    os.chdir(source)
    files = []
    for foldername, subfolders, filenames in os.walk(source):
        filenames.sort()
        for filename in sorted(filenames):
            match = mo.search(filename)
            if match:
                match = match.groups()
                newFilename = ""
                for group in match:
                    if group not in [match[1], match[2]]:
                        newFilename += group
                    elif group == match[2]:
                        number = len(files)
                        newFilename += "_" + str(number + 1)
                os.rename(filename, newFilename)
                files.append(newFilename)


if __name__ == "__main__":
    gapFiller("./Chapter_10/gapFiles")
