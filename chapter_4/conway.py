# Conway's Game of Life
import random
from re import L
import time
import copy

WIDTH = 60
HEIGHT = 20

# Create a list of lists for the cells.
nextCells = []
for x in range(WIDTH):
    column = []  # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")  # Add a living cell
        else:
            column.append(" ")  # Add a dead cell
    nextCells.append(column)  # nextCells is a list of column lists

while True:  # Main program loop.
    print("\n" * 5)  # Separate each step with newlines
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")  # pPrint the "#" or space
        print()  # Print a newline at the end of the row.

    # Calculate the next step's cells base on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighboring coordinates:
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # Count the number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbors += 1  # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == "#":
                numNeighbors += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == "#":
                numNeighbors += 1  # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == "#":
                numNeighbors += 1  # Left neighbor is alive.
            if currentCells[rightCoord][y] == "#":
                numNeighbors += 1  # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == "#":
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == "#":
                numNeighbors += 1  # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == "#":
                numNeighbors += 1  # Bottom-right neighbor is alive.

            # Set cells base on Conway's Game of Life rules:
            if currentCells[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = "#"
            elif currentCells[x][y] == " " and numNeighbors == 3:
                # Dead cells with three neighbors become alive:
                nextCells[x][y] = "#"
            else:
                # Everything else die or stays dead:
                nextCells[x][y] = " "
    time.sleep(1)  # Add a one second pause to reduce flickering
