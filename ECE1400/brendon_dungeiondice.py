import random
import numpy as np

random.seed(168)

########################################################################
# Helper Functions
########################################################################

class Dice:
    def __init__(self, sides=6):
        self.side = 0
    
    def roll(self):
        return random.randint(0,5)
        # 0 = dagger
        # 1 = shovel
        # 2 = ladder
        # 3 = lantern 
        # 4 = key
        # 5 = guard


def main():
    cards = 0
    turn = 0
    dice_1 = Dice()
    dice_1.roll()
    print(dice_1.side)


    return 0

if __name__ == "__main__":
    main()