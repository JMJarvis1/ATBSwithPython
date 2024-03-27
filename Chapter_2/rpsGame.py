import random

rpsDict = {"moves": ["rock", "paper", "scissors"],
           "score": {"wins": 0, "losses": 0, "ties": 0},
           }
title = ""

for item in rpsDict["moves"]:
    title += f"{item}, "

print(f"\n{title.rstrip(', ').upper()}\n")

playerMove = input("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit\n")

computerMove = random.choice(rpsDict["moves"])

print(computerMove, playerMove)

