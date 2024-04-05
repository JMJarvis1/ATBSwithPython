from re import M


theBoard = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}


def printBoard(theBoard):
    """Prints the game board to the screen."""
    message = "\n"
    for key, value in theBoard.items():
        if key in ["top-R", "mid-R"]:
            message += f" {value} \n---+---+---\n"
        elif key != "low-R":
            message += f" {value} |"
        else:
            message += f" {value} "
    print(message)


turn = "X"

for i in range(9):
    printBoard(theBoard)
    while True:
        move = input(f"Turn for {turn}. Move on which space?\n")
        if move in theBoard.keys():
            if theBoard[move] != " ":
                print("This space is already occupied. Choose another.\n")
                continue
            else:
                theBoard[move] = turn
                break
        else:
            print("\nInvalid move. Please try again.\n")
            continue
    turn = "O" if turn == "X" else "X"


printBoard(theBoard)
