# A simple "guess my number"-game
# Two players can play against each other, or one player can play against the
# computer. The player(s) choose a difficulty level, which determines the
# allowed number of guesses



import random

# introducing the game
print("Welcome to the number guessing game!")


# setting game mode (two-player or vs computer)
game_mode = int(input("""
Type '1' to play against the computer
Type '2' to play a 2-player game

"""))

if game_mode == 1:
    target_number = random.randint(0, 100) # against the computer
elif game_mode == 2:
    target_number = int(input("\nPick a number for the other player to guess (0-100): ")) # against another player
    while target_number > 100:
            target_number = int(input("Too high, pick a lower number: "))
    print('\033[H\033[J', end='') # clears the terminal to hide the number from the other player
    print("Ok, number stored.")
else:
    print("Unknown input - game will be terminated")
    exit(-1)


# setting difficulty (nr of allowed guesses)
difficulty = int(input("""\nSelect a difficulty level
1 - 15 allowed guesses
2 - 10 allowed guesses
3 - 5 allowed guesses

"""))

if difficulty == 1:
    max_guesses = 15
elif difficulty == 2:
    max_guesses = 10
elif difficulty == 3:
    max_guesses = 5
else:
    difficulty = print("Incorrect input - game will crash now, blame it on my developer")


# running the game
current_guesses = 0
finished = False

while not finished:
    print(f"\nYou now have {max_guesses - current_guesses} tries to guess the number")

    guess = int(input("Your guess: "))
    current_guesses += 1

    if guess == target_number:
        print(f"\nThat's correct! The number was {target_number}, and you guessed it" +
        f" in {current_guesses} guesses.")
        finished = True
    elif current_guesses == max_guesses:
        print(f"You are out of guesses, sorry! The number was {target_number}")
        finished = True
    elif guess > target_number:
        print("Nope, go lower.")
    elif guess < target_number:
        print("Nope, go higher")