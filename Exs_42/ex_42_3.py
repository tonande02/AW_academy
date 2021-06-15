punishment_text = "I will not copy-paste that from that Stackoverflow\n"
numb_of_repititions = 20

# a)
# print((punishment_text[:6] + punishment_text[10:]) * numb_of_repititions)

# b)
# print((punishment_text[:6] + punishment_text[10:].replace('paste', 'delete')) * numb_of_repititions)

# c)
print((punishment_text[:6] + punishment_text[10:].replace('paste', 'delete')) * numb_of_repititions)
print("The number of 'that's in the original sentence is:", punishment_text.count('that'))