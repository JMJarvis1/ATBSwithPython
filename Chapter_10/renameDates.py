# !Python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date
# format to European DD-MM-YYYY

import os
import re
import shutil
from pathlib import Path

# Create a regex pattern that matches files with the American date format.
datePattern = re.compile(
    r"""
                         ^(.*?)          # All text before the date. 
                         ((0|1)?\d)-     # One or two digits for the month
                         ((0|1|2|3)?\d)- # One or two digits for the day
                         ((19|20)\d\d)   # Four digits for the year
                         (.*?)$         # All text after the date.
                         """,
    re.VERBOSE,
)
p = Path.cwd() / "Chapter_10"


for amerFileName in os.listdir(p):
    mo = datePattern.search(amerFileName)

    # Skip the files without a date.
    if mo is None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename.
    euroFileName = beforePart + dayPart + "-" + monthPart + "-" + yearPart + afterPart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath(p)
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # Rename the files.
    print(
        f'Renaming "{os.path.basename(amerFileName)}" to "{os.path.basename(euroFileName)}"...'
    )
    shutil.move(amerFileName, euroFileName)  # Uncomment after testing
