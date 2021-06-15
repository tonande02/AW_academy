# Gotta catch 'em all!

import numpy


# a)
captured = tuple(['Pikachu', 'Pidgey', 'Abra', 'Pidgey', 'Eevee', 'Pidgey'])

# b)
# depends what you want to do with it, if you want to have an absolute
# unchangeable record of the pokemon he caught that day, then a tuple
# is a good choice

# c)
# print(captured.count('Pidgey'))

# d)
user_pkmon = input("Which pokemon do you want to check for? ")

if user_pkmon in captured:
    print("You have that pokemon already")
else:
    print("You don't have that pokemon")

print(f"Total pokemon: {len(captured)}")
print(f"Unique pokemon: {len(set(captured))}")