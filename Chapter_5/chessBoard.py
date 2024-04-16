import string
import random
from collections import Counter


def modelChessBoard():
    CHESS_PIECE_COUNT = {
        "pawn": 8,
        "bishop": 2,
        "knight": 2,
        "rook": 2,
        "queen": 1,
        "king": 1,
    }
    chessBoard = {}

    buildBlankBoard(chessBoard)

    boardSpaces = list(chessBoard)

    populateGamePieces(chessBoard, boardSpaces, CHESS_PIECE_COUNT.copy())

    validateBoard(chessBoard, CHESS_PIECE_COUNT)

    printGameBoard(chessBoard)


def buildBlankBoard(chessBoard):
    """Build a model of chess boartd with no pieces on it."""
    for num in sorted([x for x in range(1, 9)], reverse=True):
        for letter in list(string.ascii_uppercase[:8]):
            space = letter + str(num)
            chessBoard[space] = " "


def populateGamePieces(chessBoard, boardSpaces, chessPieceCount):
    """Allocates to each playe a random amount of each piece type and places them
    on a randomly selected space on the board.
    """
    for player in ["b", "w"]:
        for key, value in chessPieceCount.items():
            piecesRemaining = random.randint(0, value) if key != "king" else 1
            while piecesRemaining:
                gamePiece = player + key
                space = random.choice(boardSpaces)
                boardSpaces.remove(space)
                chessBoard[space] = gamePiece
                piecesRemaining -= 1


def printGameBoard(chessBoard):
    for key, value in chessBoard.items():
        if value != " ":
            print(key, value, sep=": ")


def validateBoard(chessBoard, chessPieceCount):
    # Create set ofd unique values from dict values
    gamePieces = Counter(value for value in chessBoard.values() if value != " ")

    print("Piece count: \n", gamePieces)

    for k, v in gamePieces.items():
        color = "black" if k[:1] == "b" else "white"
        pieceName = f"{color} {k[1:]}"
        maxNum = {pieceName: chessPieceCount[k[1:]]}
        minNum = 0 if k[1:] != "king" else 1
        pieceLocations = []
        message = "\n"
        if v == 1:
            plural = ""
            message += "There is "
        else:
            plural = "s"
            message += "There are "
        message += f"{v} {pieceName} piece{plural} on the board, with a maximum of "
        message += f"{maxNum[pieceName]} and a minimum of {minNum} piece{plural} "
        message += "allowed. Result: "
        if v <= maxNum[pieceName] and v >= minNum:
            message += "Pass"
        else:
            message += "Fail"
        if k == pieceName:
            pieceLocations.append(k)
        message += f"The current placement of the {chessPieceCount[k[1:]]} {pieceName}"
        message += f"{plural} are "
        for location in pieceLocations:
            message += location
            if location != pieceLocations[-1]:
                message += ", "
            else:
                message += "."
        print(message + "\n")


if __name__ == "__main__":
    modelChessBoard()
# message += " "
# for x in range(64):
#     message =


# message = ""
# for x in range(17):
#     if x == 0 or x % 4 in [0, 2]:
#         message += ("* * * * " * 8) + "* \n"
#     else:
#         message += (("*       " * 8) + "*\n") * 3

# print(message)
