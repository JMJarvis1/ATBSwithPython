#! Python3
# Exercise program -- os.walk()

import os
from pathlib import Path


p = Path.cwd() / "Chapter_10"
os.chdir(p)

for folderName, subfolders, fileNames in os.walk(p):
    message = f"The current folder is {folderName}\n"

    for subfolder in subfolders:
        message += f"  SUBFOLDER OF {os.path.basename(folderName)}: {subfolder}\n"

    for fileName in fileNames:
        message += f"  FILE INSIDE {os.path.basename(folderName)}: {fileName}\n"
        message += f"\t The first line of text in {fileName} is:\n"

    print(message + "\n")
