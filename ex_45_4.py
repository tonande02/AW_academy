list_of_lists = [1, [2, 3, "4"], [5, [6, "7", 8], 9, 10]]
print(list_of_lists)

list_of_lists[1][2] = int(list_of_lists[1][2])
list_of_lists[2][1][1] = int(list_of_lists[2][1][1])
print(list_of_lists)