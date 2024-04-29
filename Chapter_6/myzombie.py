import zombiedice
import random

class MyZombie:
    def __init__(self, name) -> None:
        # All zombies must have a name.
        self.name = name

    def turn(self, gameState):
        # GamgeState is a dict with info about the current state of the game.
        # You can ognore it in your code if you want to.

        diceRollResults = zombiedice.roll() # First roll.
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'foosteps' with how many rolls of each type there were. 
        # The 'rolls' key is a list of (color, icon) tuples with the
        # excact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1, 
        # 'rolls': [('yelllow', 'brains'), ('red', 'footsteps'),
        #           ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH CODE WITH YOUR OWN:
        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            
            rollAgain = random.randint(0,1)
    
            if shotguns > brains:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name="Until Leading"),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Until 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name="Until 1 Shotgun",  minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Un comment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies = zombies, numGames=1000)
    