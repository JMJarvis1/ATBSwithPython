import random
import sys


def play_rps():

    rpsDict = {
        "choice": ["rock", "paper", "scissors", "quit"],
        "moves": ["r", "p", "s", "q"],
        "score": {"wins": 0, "losses": 0, "ties": 0},
    }

    run_game_loop(rpsDict)


def print_title(rpsDict: dict) -> None:
    """Prints the game title, neatly formatted.

    Args:
        rpsDict (dict): dictionary with game info for rps game.
    """
    title = ""
    for item in rpsDict["choice"]:
        title += f"{item}, "
    print(f"\n{title.rstrip(', ').upper()}\n")


def run_game_loop(rpsDict):
    while True:
        move_menu = "\nEnter your move: (r)ock, (p)aper, (s)cissors, or (q)uit\n"
        playerMove = input(move_menu).lower()

        computerMove = random.choice(rpsDict["moves"][:2])

        if playerMove.lower() not in rpsDict["moves"]:
            continue  # Restart loop for invalid choice
        elif playerMove == "q":  # Quits game.
            quit_game(rpsDict)

        compare_moves(rpsDict, playerMove, computerMove)


def quit_game(rpsDict):

    if sum(rpsDict["score"].values()) > 0:
        print("\n****** Final Score *****\n")
        display_score(rpsDict)
        print("************************")
        sys.exit()


def compare_moves(rpsDict, playerMove, computerMove):

    # Tuple holding location of player and comp. moves relative to rpsDict location
    moves = (
        rpsDict["moves"].index(playerMove),
        rpsDict["moves"].index(computerMove),
    )

    display_moves(rpsDict, moves)

    if moves[0] == moves[1] - 1:  # If playerMove is one index higher in rpsdict.
        print("You win!\n")
        score_game(rpsDict, "wins")
    elif moves[0] == moves[1]:  # Tie: playerMove == computerMove
        print("It's a tie!\n")
        score_game(rpsDict, "ties")
    else:
        print("You lose!\n")
        score_game(rpsDict, "losses")

    display_score(rpsDict)


def display_moves(rpsDict, moves):
    message = f"\n{rpsDict['choice'][moves[0]].upper()} versus...\n"
    message += f"{rpsDict['choice'][moves[1]].upper()}\n"
    print(message)


def score_game(rpsDict: dict, condition: str):
    rpsDict["score"][condition] += 1


def display_score(rpsDict):
    scores = rpsDict["score"]
    message = ""
    for score in scores.items():
        message += f"{score[1]} {score[0].title()}, "
    message = message.rstrip(", ")
    print(message)


if __name__ == "__main__":
    rpsDict = play_rps()
