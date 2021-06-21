# The user dictionary program - now with save functionality
# only done a) (ish)


print("""
Welcome to your dictionary! Please add an entry to begin,
or 'revert' to exit and see your dictionary\n""")

dict_file = open(file='my_dict.txt', mode='a')
user_dict = {}
new_entry = ""

# creating the user dictionary
while new_entry.lower() != "revert":
    new_entry = input("Enter next pair (key;value)  or 'revert': ")
    if new_entry == "revert":
        break
    else:
        try:
            entry = new_entry.split(";")
            user_dict[entry[0]] = entry[1]
            dict_file.write(f"{entry[0]} : {entry[1]} \n")
        except:
            print("Wrong input, please try again")
            continue

dict_file.close()

print()
with open(file='my_dict.txt', mode='r') as read_dict:
    for line in read_dict:
        print(line, end='')