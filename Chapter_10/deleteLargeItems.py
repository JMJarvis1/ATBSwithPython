#! Python3 renameLargeItems.py -- ATBS with Python Project for Ch. 10
#  Program walks throuhg a folder tree, finding files or folders larger
#  than 100 GB, then marks them for deletion.

import sys
import os

# import send2trash


def deleteLargeItems(folder):
    """Walk throuhg a folder tree, finding files or folders larger
    than 100 GB, then marks them for deletion. Prints

        Args:
            folder (str): path to folder that will be searched
    """
    # Walk through file tree
    for foldername, subfolders, filenames in os.walk(folder):
        for subfolder in subfolders:
            removeItem(foldername, subfolder)  # Remove large subfolders

        for filename in filenames:
            removeItem(foldername, filename)  # Remove large files

    sys.exit()


def removeItem(foldername, item):
    """Check ite's size and then deletes it if it is over 100GB

    Args:
        foldername (str): path to folder containing item
        item (str): path subfolder or file
    """
    p = os.path.join(foldername, item)

    byteSize = os.path.getsize(p)
    mbSize = byteSize / (1024**2)
    if mbSize > 100:
        relPath = os.path.relpath(item)
        print(f"Deleting {relPath}: {round(mbSize,0)}GB")
        # send2trash.send2trash(os.path.join(foldername, item))


if __name__ == "__main__":
    try:
        deleteLargeItems("./Chapter_10/largeItems")
    except FileNotFoundError:
        sys.exit()
