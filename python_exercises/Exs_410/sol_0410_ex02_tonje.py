# A program for reading company stock info from a .csv-file

import time
import datetime

# opening the file
stock_file = open(file='SP_20_21.csv', mode='r')

# placing the column names in a list
columns = stock_file.readline().split()
columns = columns[0].split(',') + columns[1].split(',')
# columns.pop(0)
print(columns)

# a function that takes a single line entry from the csv-file, and returns
# the date and its values in a dictionary
# def convert_entry(line):
#     line = line[0].split(',')
#     # print(len(line), line)

#     return_date = line[0]
#     print(return_date)

#     date_dict = {}
#     for column in columns


# for line in range(5):
#     read_line = stock_file.readline().split()
#     convert_entry(read_line)



stock_file.close()