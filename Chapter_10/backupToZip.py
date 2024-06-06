#! Python3 backuptoZip.py - Copies an entire folder and its content
#  into a ZIP file whose filename increments.

import zipfile
import os
from pathlib import Path


def backupToZip(folder):
    # Back up the entire contents of 'folder' into ZIP file.

    folder = Path(folder)  # Make sure folder is absolute.
    parent = folder.parent
    # Figure out the filename this code should use based on what files
    # already exit.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"

        if not Path.exists(parent / zipFilename):
            break
        number += 1

    # Create the ZIP file.
    print(f"Creating {zipFilename}...")

    backupZip = zipfile.ZipFile(parent / zipFilename, "w")

    # Walk the entire folder tree and compress the files in each folder.

    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")
        # Add the current folder to the ZIP file.
        backupZip.write(f"{foldername}")

        # Add all of the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue  # Don't backup the backup ZIP files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print("Done")


backupToZip("/Users/johnmichaeljarvis/Documents/GitHub/ATBSwithPython/Chapter_10")
