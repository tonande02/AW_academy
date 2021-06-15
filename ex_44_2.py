# Yahtzee checker

import random

s1 = random.randint(1, 6)
s2 = random.randint(1, 6)
s3 = random.randint(1, 6)
s4 = random.randint(1, 6)
s5 = random.randint(1, 6)
s6 = random.randint(1, 6)


if s1 == s2 == s3 == s4 == s5 == s6:
    print(f"Wow, you got yahtzee in one! Amazing! {s1} is your lucky number!")
else:
    print("\nSorry, no yahtzee for you... Let's keep trying until we get there!\n")
    # print(s1, s2, s3, s4, s5, s6)


count = 0
while not (s1 == s2 == s3 == s4 == s5 == s6):
    count += 1

    if count % 1000 == 0:
        print(f"Nothing in {count} tries...")
        
        

    s1 = random.randint(1, 6)
    s2 = random.randint(1, 6)
    s3 = random.randint(1, 6)
    s4 = random.randint(1, 6)
    s5 = random.randint(1, 6)
    s6 = random.randint(1, 6)

print(f"\nFinally! You got yahtzee on {s1} in {count} tries. Success!!")