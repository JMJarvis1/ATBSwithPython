"""winsome, lose some"""

import random
import math


def flipCoins():
    COIN_SIDES = ("T", "H")  # "Tails"/"Heads"
    FLIPS = 10_000  # Number of flips to peform.
    STREAK_LENGHTH = 6  # Length of run to count as a streak (T/H)

    results = generateFlips(FLIPS, COIN_SIDES)
    winRatios, winCounts = getWinData(results)  # [Tails%, Heads%]
    streakCount, streakMax = getStreakData(STREAK_LENGHTH, results)

    displayStats(
        COIN_SIDES, FLIPS, results, winRatios, winCounts, streakCount, streakMax
    )


def generateFlips(flips, coinSides) -> list:
    """Generate a list holding the outcome of a set number of coin flips."""
    results = []
    for flip in range(flips):
        results.append(random.choice(coinSides))
    return results


def getWinData(results):
    """Checks the results and calculates the win percenatages for Tails and Heads."""
    tailWins = 0
    headWins = 0
    for result in results:
        if result == "T":
            tailWins += 1
        else:
            headWins += 1
    # tailRatio = tailWins/len(results)
    # headRatio = headWins / len(results)

    return [(x / len(results)) * 100 for x in [tailWins, headWins]], [
        tailWins,
        headWins,
    ]


def getStreakData(streak_length, results) -> list:
    """Checks the results for streaks, returns counts"""
    streakCount = [0, 0]  # Total streaks [Tails, Heads]
    streakMax = [0, 0]  # Longest streak [Tails, Heads]

    for index, flip in enumerate(results):
        min_streak = index + streak_length  # Minimum run for streak to count
        sample = results[index:min_streak]

        if sample != [flip for x in sample]:
            continue
        else:
            if flip == "T":
                streakCount[0] += 1
                streakMax[0] = getStreakLength(
                    streakMax[0], results, flip, min_streak, sample
                )
            else:
                streakCount[1] += 1
                streakMax[1] = getStreakLength(
                    streakMax[1], results, flip, min_streak, sample
                )
    return streakCount, streakMax


def getStreakLength(streakMax, results, flip, location, sample) -> list:
    new_streak = len(sample)
    while True:
        for index, toss in enumerate((results[location + 1 :])):
            if toss != flip:
                break
            new_streak += 1
        break
    if new_streak > streakMax:
        return new_streak
    else:
        return streakMax


def displayStats(
    coin_sides, flips, results, winRatios, winCounts, streakCount, StreakMax
):
    """Displays stats for flips performed."""

    message = f"\n\t{'*' * 8} Results for {flips:,} Coin Flips {'*' * 8}\n\n\t    "
    message += " \tTails\t\t\t"
    message += "Heads\n\t\t"
    message += f"Wins: {winCounts[0]}\t\t"
    message += f"Wins: {winCounts[1]}\n\t\t"
    message += f"Win %: {winRatios[0]:.2f}\t\t"
    message += f"Win %:({winRatios[1]:.2f})\t\n\t\t"
    message += f"Number of streaks: {streakCount[0]}\t"
    message += f"Number of streaks: {streakCount[1]}\n\t\t"
    message += f"Longest Streak: {StreakMax[0]}\t"
    message += f"Longest Streak: {StreakMax[1]}\t"
    message += gridVisualization(results)

    print(message)

    # Print a square visual representation of the results


def gridVisualization(results) -> str:
    sampleResults = random.sample(results, 1000)
    gridWidth = int(2 * (math.sqrt(len(sampleResults))))
    gridHeight = int((math.sqrt(len(sampleResults))) / 2)

    grid = "\n\n"

    i = 0
    for y in range(gridHeight):
        for x in range(gridWidth):  # Prints row of results
            grid += f"{sampleResults[i]}"
            i += 1
        grid += "\n"  # Starts new line

    return grid


if __name__ == "__main__":
    flipCoins()
