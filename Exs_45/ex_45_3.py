# Quantile calculator

import random

# a)
# i & ii)
values = []
alpha = 0.42

for i in range(25):
    values.append(random.randint(0, 50))


# b)
values = sorted(values)
print(values)
print()

# c)
lower_idx = round(len(values)*alpha/2)
upper_idx = round(len(values)*(1-alpha/2))-1

print(f"Lower index: {lower_idx}")
print(f"Upper index: {upper_idx}")
print()

# d)
lower_value = values[lower_idx]
upper_value = values[upper_idx]

print(f"Lower value: {lower_value}")
print(f"Upper value: {upper_value}")