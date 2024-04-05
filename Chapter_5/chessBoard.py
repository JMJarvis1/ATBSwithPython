import string

chessPieces = {}
chessBoard = {}

# chessBoard = {
#     "A": [ x for x in range(1, 14)]
# }

for num in sorted([x for x in range(1, 9)], reverse=True):
    for letter in list(string.ascii_uppercase[:8]):
        space = letter + str(num)
        chessBoard[space] = " "

print(chessBoard)

message += " "
for x in range(64):
    message =


message = ""
for x in range(17):
    if x == 0 or x % 4 in [0, 2]:
        message += ("* * * * " * 8) + "* \n"
    else:
        message += (("*       " * 8) + "*\n") * 3

print(message)
