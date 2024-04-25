"""Blackjack (barebones version)
by Al Sweigart al@inventwithpython.com
The classic card game also known as 21."""

import random

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def main():
    print("Blackjack (barebones version)")
    print("by Al Sweigart al@inventwithpython.com")

    # Create a deck of cards
    deck = []
    for rank in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
        for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]:
            deck.append([rank, suit])
    random.shuffle(deck)

    # Give the dealer and player two cards each
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    # Handle player actions:
    while True:  # Keep looping until player stands or busts.
        displayHands(playerHand, [["??", "?"]] + dealerHand[1:])
        print()

        if getHandValue(playerHand) > 21:
            break  # Player has busted

        # Get the player's move, either "H" or "S":
        move = input("H or S > ").upper()

        if move == "H":
            # Hitting takes another card
            newCard = deck.pop()
            print(f"You drew a {newCard[0]} of {newCard[1]}")
            playerHand.append(newCard)

            if getHandValue(playerHand) > 21:
                continue  # player has busted
        elif move == "S":
            break  # Staying ends player's turn

    # Handle the dealer's actions:
    if getHandValue(dealerHand) <= 21:
        while getHandValue(dealerHand) < 17:
            print("Dealer hits...")
            dealerHand.append(deck.pop())
            displayHands(playerHand, [["??", "?"]] + dealerHand[1])

            if getHandValue(dealerHand) > 21:
                break  # Dealer has busted
            input("Press enter to continue...")

    # Show the final hands:
    displayHands(playerHand, dealerHand)

    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)

    if dealerValue > 21:
        print("Dealer busts! You won!")
    elif playerValue > 21 or (playerValue < dealerValue):
        print("You bust!")
    elif playerValue > dealerValue:
        print("You won!")
    elif playerValue == dealerValue:
        print("It is a tie!")


def displayHands(playerHand, dealerHand):
    print("DEALER:")
    displayCards(dealerHand)
    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(allCards):
    value = 0
    numberOfAces = 0

    # Add the value of the non-ace cards
    for card in allCards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1  # Aces can be worth 1 or 11 points
        elif rank in ["K", "Q", "J"]:
            value += 10  # Facecards are worth 10 points
        elif rank in ["1", "2", "3", "5", "6", "7", "8", "9", "10"]:
            value += int(rank)  # Numbered cards are worth their number.

    # Add the value of the ace cards:
    value += numberOfAces
    for i in range(numberOfAces):
        # If another 10 can be added without busting, add it:
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(allCards):
    rows = ["", "", "", "", ""]

    for card in allCards:
        rank = card[0]
        suit = card[1]
        rows[0] += " ___ "  # The row to display for the top of each card
        rows[1] += f"|{rank.ljust(2)} | "
        rows[2] += f"| {suit} | "
        rows[3] += f"|_{rank.rjust(2, '_')}| "

        for row in rows:
            print(row)


# Call the main() function to play the game:
if __name__ == "__main__":
    main()
