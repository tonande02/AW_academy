# A program that lets the user create their own dictionary

# setting up and introducing the program to the user
user_dict = {}
new_entry = ""

print("""
Welcome to your dictionary! Please add an entry to begin,
or 'revert' to exit and see your dictionary\n""")


# creating the user dictionary
while new_entry.lower() != "revert":
    new_entry = input("Enter next pair (key;value)  or 'revert': ")
    if new_entry == "revert":
        break
    else:
        try:
            entry = new_entry.split(";")
            if entry[0] in user_dict:
                user_dict[entry[0]] += (entry[1])
            else:
                user_dict[entry[0]] = entry[1]
        except:
            print("Wrong input, please try again")
            continue

# activate to check that the above works
# print()
# print(user_dict)


# creating and printing the reverted dictionary
new_dict = {}
for key in user_dict:
    new_dict[user_dict[key]] = key

print()
print("""Here is your dictionary backwards.
(Blame my developer if you're not happy)\n""")
print(new_dict)