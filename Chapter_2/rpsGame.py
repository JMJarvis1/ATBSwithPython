import random
import sys


def play_rps():
    """Run a session of the Rock, Paper, Scissors game."""
    rpsDict = {
        "choice": ["rock", "paper", "scissors", "quit"],
        "moves": ["r", "p", "s", "q"],
        "score": {"wins": 0, "losses": 0, "ties": 0},
    }

    print_title(rpsDict)

    run_game_loop(rpsDict)


def print_title(rpsDict: dict) -> None:
    """Print the game title, neatly formatted.

    Args:
        rpsDict (dict): dictionary with game info for rps game.
    """
    title = ""
    for item in rpsDict["choice"][:3]:
        title += f"{item}, "
    print(f"\n{title.rstrip(', ').upper()}\n")


def run_game_loop(rpsDict: dict) -> None:
    """Maintain game loop until user quits.

    Args:
        rpsDict (dict): dictionary with game info for rps game.
    """
    while True:
        move_menu = "\nEnter your move: (r)ock, (p)aper, (s)cissors, or (q)uit\n"

        playerMove = input(move_menu).lower()
        computerMove = random.choice(rpsDict["moves"][:3])

        match playerMove:
            case "r" | "p" | "s":
                compare_moves(rpsDict, playerMove, computerMove)
            case "q":
                quit_game(rpsDict)  # Quit game and display scores for games played.
            case _:
                continue  # Restart loop for invalid choice


def quit_game(rpsDict: dict) -> None:
    """Quit game at user command.

    Args:
        rpsDict (dict): dictionary with game info for rps game.
    """
    if sum(rpsDict["score"].values()) > 0:
        print("\n****** Final Score ******")
        display_score(rpsDict)
        print("*************************")
    sys.exit()


def compare_moves(rpsDict: dict, playerMove: str, computerMove: str) -> None:
    """Compare the player's move versus the computer's and decide win, loss, or tie.

    Args:
        rpsDict (dict): dictionary with game info for rps game.
        playerMove (str): the player's move (r, p, or s)
        computerMove (str): the computer's move (r, p, or s)
    """
    # Tuple holding location of player and comp. moves relative to rpsDict location
    moves = (
        rpsDict["moves"].index(playerMove),
        rpsDict["moves"].index(computerMove),
    )

    display_moves(rpsDict, moves)

    game_state = playerMove + computerMove

    player_win_conditons = ["rs", "pr", "sp"]

    if game_state in player_win_conditons:
        condition = "wins"
    elif playerMove == computerMove:
        condition = "ties"
    else:
        condition = "losses"
    score_game(rpsDict, condition)

    display_score(rpsDict)


def display_moves(rpsDict: dict, moves: tuple) -> None:
    """Display the player vs. computer moves for current game

    Args:
        rpsDict (dict): dictionary with game info for rps game.
        moves (tuple): tuple of game moves indexed to rpsDict location
    """
    message = f"\n{rpsDict['choice'][moves[0]].upper()} versus...\n"
    message += f"{rpsDict['choice'][moves[1]].upper()}\n"
    print(message)


def score_game(rpsDict: dict, condition: str) -> None:
    """Edits "score" entry in rpsDict to reflect outcome of current match.

    Args:
        rpsDict (dict): dictionary with game info for rps game.
        condition (str): "wins", "ties", "losses"
    """
    rpsDict["score"][condition] += 1


def display_score(rpsDict: dict) -> None:
    """Displays rpsDict["scores"] entry, neatly formatted.

    Args:
        rpsDict (dict): dictionary with game info for rps game.
    """
    scores = rpsDict["score"]
    message = ""
    for score in scores.items():
        message += f"{score[1]} {score[0].title()}, "
    message = message.rstrip(", ")
    print(message)


if __name__ == "__main__":
    rpsDict = play_rps()
