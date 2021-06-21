import time

# testing - might come back to implement this later
# load_bar = list("|        |")
# pos = 1

# while pos < len(load_bar):
#     # list[pos] = "="
#     # pos += 1
#     # print(load_bar.join())
#     print(load_bar[pos])
#     pos += 1


print("|      |", flush=True, end='\r')
time.sleep(1)
print("|=>    |", flush=True, end='\r')
time.sleep(1)
print("|==>   |", flush=True, end='\r')
time.sleep(1)
print("|===>  |", flush=True, end='\r')
time.sleep(1)
print("|====> |", flush=True, end='\r')
time.sleep(1)
print("|=====>|", flush=True, end='\r')
time.sleep(1)
print("|======|", flush=True, end='\r')
time.sleep(1)