# A program that merges dictionaries

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

# this line unpacks the key-value pairs in each dictionary, and places them
# in the merged_dict
merged_dict = {**dic1, **dic2, **dic3}

print(merged_dict)