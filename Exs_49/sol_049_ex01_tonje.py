# The yahtzee program in dictionary form
# the program keeps running until there is only one entry in the dictionary:
# the first throw to get yahtzee
# it also counts nr of tries to get yahtzee


import random

dice = {}
tries = 0

while len(dice) != 1:
    dice = {}
    tries += 1
    side = 1

    for i in range(5):
        value = random.randint(1,6)
        dice[value] = f"side {value}"
        side += 1
    
    # activate to check that the program doesn't register non-yahtzee throws
    # if tries % 200 == 0:
    #     print(f"No yahtzee with try nr {tries}: {dice}")

print()
print(f"You finally got yahtzee on {dice[value]}, in {tries} tries")