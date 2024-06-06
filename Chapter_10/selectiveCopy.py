#! Python3 selectiveCopy.py - Walk through a folder tree, searching for
#  files of a given extension (ie. '.txt', '.pdf') and copies them into a new folder.

import shutil
import os
from pathlib import Path
import sys


def selectiveCopy(extension: str):
    """Copy certain files to a folder based on file's extension.

    Args:
        extension (str): File type extension ie. '.txt'
    """
    p = os.path.abspath("selectiveCopy.py")
    sourceDir = Path(p).parent
    destinationDir = os.path.join(sourceDir / "copy_folder")

    files = []  # Hold filenames for files matching extension.

    if not Path(destinationDir).exists():
        os.mkdir(destinationDir)

    searchByExtension(extension, sourceDir, files)
    copyFilesToNewDirectory(destinationDir, files)

    sys.exit()


def searchByExtension(extension, source, files):
    """Walk the source folder, add files w/ matching extensions to list.

    Args:
        extension (str): File type extension ie. '.txt'
        source (str): Top level directory where search begins
        files (list): Files w/ matching extension.
    """
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith(extension):
                files.append(os.path.join(foldername, filename))


def copyFilesToNewDirectory(destinationDir, files):
    """Copy files to new folder in top level directory

    Args:
        destinationDir (str): path to detination folder
        files (list): Files w/ matching extension.
    """
    for file in files:
        file = os.path.abspath(file)
        fName = os.path.basename(file)
        print(f"Copying {fName} to folder: {os.path.basename(destinationDir)}")
        try:
            shutil.copy(file, destinationDir)
        except shutil.SameFileError:
            continue


if __name__ == "__main__":
    selectiveCopy(".txt")
