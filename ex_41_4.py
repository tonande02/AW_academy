import time

# load_bar = list("|        |")
# pos = 1

# while pos < len(load_bar):
#     # list[pos] = "="
#     # pos += 1
#     # print(load_bar.join())
#     print(load_bar[pos])
#     pos += 1

# print("|      |", end="", flush=True)
# time.sleep(1)
# print("|=>    |", end="", flush=True)
# time.sleep(1)
# print("|==>   |", end="", flush=True)
# time.sleep(1)
# print("|===>  |", end="", flush=True)
# time.sleep(1)
# print("|====> |", end="", flush=True)
# time.sleep(1)
# print("|=====>|", end="", flush=True)
# time.sleep(1)
# print("|======|", end="", flush=True)
# time.sleep(1)


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