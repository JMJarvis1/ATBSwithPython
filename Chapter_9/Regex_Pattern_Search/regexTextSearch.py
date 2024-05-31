# !Python3
r"""
regexTextSearch.py - Allows user to search all .txt files in directory
                 for any match to a regular expression supplied by
                 the user. The program then prints the fisrt line
                 from the text that contains the expression and
                 prints it to the screeen.

                             **Example**
  <Prompt>
  Please enter a regular expression:
  <User Input>
   >>>\b(0[1-9]|1[012])([. / -])(0[1-9]|[12][0-9]|3[01])\2((19|20)...
      ...\d{2})\b
  Results for hitchHikersGuideInfo.txt:
  Line 102:
       "Hitchiker's Guide to the Galaxy
            ...was first published on 10/11/1979."
  Line 42:
      "The world was destroyed on 10/11/1979."

    --------
    sys.argv
    --------
        '--test': Run program with the '--test' argument to create a
                  random number of dummy search files containing a
                  randomly generated list of names and birthdates.
"""

import re
import sys
import os
import platform
import rstr
import pyperclip
import textwrap
import random as rd
import pyinputplus as pyip
from pathlib import Path


def main():
    clearScreen()

    printHeaderText()  # Display program info and use instructions

    currentDir = getPathToParent()  # Gets path to program's parent.

    os.chdir(currentDir)

    txtFiles = list(currentDir.glob("*.txt"))  # List of txt files in current directory.

    if not len(txtFiles) > 0:  # Current directory has no txt files to search
        txtFiles = handleNoFilesForSearch(currentDir)

    userRegex = getRegexFromUser()  # Returns compiled regex pattern

    # Match file(s) content to user pattern
    matches = findMatches(userRegex, txtFiles)

    displayInitialResult(currentDir, matches)

    detailedResultsMsg = createDetailedResultsMsg(matches)

    userMenuLoop(currentDir, detailedResultsMsg)

    clearScreen()
    sys.exit()


def userMenuLoop(currentDir, detailedResultsMsg):
    """Present menu options to user, respond, and loop back to get next
    selection.

    Args:
        currentDir (Path): abs. path to parent dir. of program
        detailedResultsMsg (str): Formatted output from search
    """
    while True:
        response = getUserMenuSelection()
        match response:
            case "Copy results to clipboard.":
                try:
                    pyperclip.copy(detailedResultsMsg)
                except pyperclip.PyperclipException:
                    errorMessage = "\nFile could not be copied to clipboard.\n"
                    errorMessage += "\tPyperclip could not find a copy/paste mechanism for your system.\n"
                    errorMessage += "\tFor more information, please visit:\n\thttps://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error\n\n"
                    print(errorMessage)
            case "Save results to file.":
                saveFile = createSaveFile(currentDir, detailedResultsMsg)
                print(f"\nResults written to {saveFile}.txt\n")
            case "Print to screen.":
                print(detailedResultsMsg)
            case "Start new search.":
                main()
            case "Quit.":
                print("Quitting...")
                break


def handleNoFilesForSearch(currentDir):
    """Handle error resulting from there not being a txt file in the
    current directory in which to search for matches to user pattern.

    Args:
        currentDir (Path): abs. path to parent dir. of program

    Returns:
        _type_: _description_
    """
    if len(sys.argv) > 1 and sys.argv[1].lower() == "--test":
        txtFiles = createTestFiles(currentDir)  # Create test .txt files
    else:
        noFilesMsg = f"There are no .txt files available in the current working directory ({currentDir}). Please ensure that the files are present or append the '--test' argument to your commmand when running regexTextSearch.py if you wish to create some test files to search."
        print(
            textwrap.fill(
                noFilesMsg,
                72,
                initial_indent="  ",
                subsequent_indent="  ",
            ),
            "\n",
        )
        sys.exit()
    return txtFiles


def clearScreen():
    match platform.system():
        case "Windows":
            os.system("cls")
        case "Linux":
            os.system("clear")
        case _:
            print("Error: Operating system cannot be determined.")
            sys.exit()


def printHeaderText():
    """Display the program's hearder outlining the purpose of the
    program and it's use."""

    headerText = " Regex Search ".center(72, "-")
    headerText += "\n\n"
    headerText += """
    Search all .txt files in the current directory for any match to a 
    regular expression supplied by the user. The program then extracts 
    the first line from text that contains a value matching the regular
    expression and prints it to the screen.\n\n""".center(72)
    headerText += "**Example**".center(72)
    headerText += r"""
    <Prompt>
      Please enter a regular expression:
    <User Input>
      >>>\b(0[1-9]|1[012])([. / -])(0[1-9]|[12][0-9]|3[01])\2((19|20)...
        ...\d{2})\b
    <Displayed Result>
      Results for hitchHikersGuideInfo.txt:
        Line 102:
            "Hitchiker's Guide to the Galaxy
                 ...was first published on 10/11/1979."
        Line 42: 
            "The world was destroyed on 10/11/1979."
""".rjust(79)
    headerText += "\n" + "(c) 2024 John Michael Jarvis".rjust(72)
    headerText += "\n" + "".center(72, "-") + "\n"

    print(headerText)


def getRegexFromUser():
    """Prompts user for a regex string, validates the input before
       returning the response.

    Returns:
        string: the regular expression string provided by the user.
    """

    prompt = "\nPlease enter a regular expression: \n"
    response = pyip.inputRegexStr(prompt)

    return response


def getPathToParent():
    """Calculates and returns the path of the program's parent directory.

    Returns:
        Path: absolute path to parent directory
    """
    for r, d, f in os.walk(Path.cwd()):
        for file in f:
            if file == "regexTextSearch.py":
                filePath = os.path.join(r, file)
                p = Path(filePath)
                parentPath = p.parent.absolute()
    return parentPath


def createTestFiles(currentDir):
    """Generate a random number of dummy txt files containing a random
        number of randomly generated first name / last name pairs, with
        each name pair having a randomly generated birthdate.

    Args:
        currentDir (Path): abs. path to parent dir. of program

    Returns:
        list: Containing names of created files.
    """
    dateGenerator = re.compile(
        r"\b(0[1-9]|1[012])([./-])(0[1-9]|[12][0-9]|3[01])\2((19|20)\d{2})\b"
    )
    with open("test_files/last-names.txt", "r") as file:
        lastNames = file.read().splitlines()
        with open("test_files/first-names.txt", "r") as file:
            firstNames = file.read().splitlines()

            for i in range(rd.randint(2, 6)):
                with open(f"testText_{i + 1}.txt", "w") as testFile:
                    for i in range(rd.randint(50, 500)):
                        randomDate = rstr.xeger(dateGenerator)
                        name = f"{rd.choice(lastNames)}, {rd.choice(firstNames)}"
                        testFile.write(f"{name.title()}: {randomDate}\n")
        createdFiles = list(currentDir.glob("*.txt"))
    return createdFiles


def findMatches(userRegex, txtFiles):
    """Use regex pattern search to search txt files in current
        directory for matches to user supplied regex pattern.

    Args:
        userRegex (str): User supplied regular expression string
        txtFiles (list): list of txt files in current directory

    Returns:
        dict: Key = File name, Values = [match location, matched text]
    """
    matches = {}
    for txtFile in txtFiles:
        fileName = os.path.basename(txtFile)
        matches[fileName] = []
        with open(txtFile) as f:
            for index, line in enumerate(f.readlines()):
                line = line.rstrip("\n")
                if re.search(userRegex, line):
                    matches[fileName].append([index + 1, line])
    return matches


def displayInitialResult(currentDir, matches):
    """Display the count of regex pattern matches in each file.

    Args:
        currentDir (Path): abs. path to parent dir. of program
        matches (dict): K:File name, V:[match location, matched text]
    """
    message = f"\nA regex pattern search of the text files in {currentDir} found: \n\n"

    for fileName, matchList in matches.items():
        message += f"{len(matchList)} matches in {fileName}\n"

    print(message)


def createDetailedResultsMsg(matches):
    """Create formatted string with detailed result from search.

    Args:
        matches (dict): K:File name, V:[match location, matched text]

    Returns:
        str: Formatted search results
    """
    message = ""

    for fileName, matchList in matches.items():
        message += f"\nResults for {fileName}:\n"
        if len(matchList) > 0:
            for item in matchList:
                message += f"  Line {item[0]}:\n\t{item[1]}\n"
        else:
            message += "  No Matches Found.\n"
    return message


def getUserMenuSelection():
    """Request and validate user selection from the program menu.

    Returns:
        str: user menu choice
    """
    choices = [
        "Copy results to clipboard.",
        "Save results to file.",
        "Print to screen.",
        "Start new search.",
        "Quit.",
    ]

    prompt = f"Please chooose an option below (1-{len(choices)}): \n"

    response = pyip.inputMenu(choices, prompt, numbered=True)
    return response


def createSaveFile(currentDir, detailedResultsMsg):
    """Save formatted details of search results to txt file to
    current dirctory.

    Args:
        currentDir (Path): abs. path to parent dir. of program
        detailedResultsMsg (str): formatted details from search.

    Returns:
        str: validated file name that results were saved to
    """
    saveFile = pyip.inputFilename(
        "Choose a filename (Do Not include and extension.):\n> ",
        "results",
        limit=10,
    )
    with open(currentDir / (saveFile + ".txt"), "w") as f:
        f.write(detailedResultsMsg)
    return saveFile


if __name__ == "__main__":
    main()
