import random

dice = [1, 2, 3, 4, 5, 6]
n_dice = 5

rand_dices = []

for i in range(n_dice):
    rand_dices.append(random.choice(dice))

print(f"Your dices are: {sorted(rand_dices)}")
print(f"Your lowest dice is: {min(rand_dices)}")
print(f"Your highest dice is: {max(rand_dices)}")
print()

if all(d == rand_dices[0] for d in rand_dices):
    print("Yahtzee, woohoo!")
else:
    print("No yahtzee, boohoo... Go again!\n")


# Checking that it works if the player gets Yahtzee
tries = 0
while not all(d == rand_dices[0] for d in rand_dices):
    tries += 1
    rand_dices = []
    count = 0
    while count < n_dice:
        rand_dices.append(random.choice(dice))
        count += 1

print(f"\nFinally! You got yahtzee on {rand_dices[0]} in {tries} tries. Success!!")
print(rand_dices)