'''dungeon dice program'''
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

def roll_of_1_die():
    return random.randint(0,5)

def rolldice(x):
    if x == 6:
        return [roll_of_1_die(),roll_of_1_die(),roll_of_1_die(),roll_of_1_die(),roll_of_1_die(),roll_of_1_die(),]
    if x == 5:
        return [roll_of_1_die(),roll_of_1_die(),roll_of_1_die(),roll_of_1_die(),roll_of_1_die()]
    if x == 4:
        return [roll_of_1_die(),roll_of_1_die(),roll_of_1_die(),roll_of_1_die()]
    if x == 3:
        return [roll_of_1_die(),roll_of_1_die(),roll_of_1_die()]
    if x == 2:
        return [roll_of_1_die(),roll_of_1_die()]
    if x == 1:
        return [roll_of_1_die()]

rolldice(6)

'''this is the chat GPT way to roll the dice'''
# def roll_die():
#     """Roll a single die (returns a symbol)."""
#     return random.randint(0, 5)

# def roll_dice(n):
#     """Roll n dice."""
#     return [roll_die() for _ in range(n)]

########################################################################
# Main
########################################################################

def main():
    cards = 0
    turn = 0
    dice_1 = Dice()
    dice_1.roll()
    print(dice_1.side)

    print(turn, cards)

    while cards < 8:
        turn += 1
        earned = 0
        wall = []
        pit = rolldice(6)

        # still need to figure out how to seperate duplicate dice from solo dice

        if newpit < oldpit:
            if 3 zeros:
                cards = cards - 1
                print ('3 guards')
    
    return 0

if __name__ == "__main__":
    main()
            