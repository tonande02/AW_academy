# random group generator

import random

students = [
    "Anders",
    "Ole",
    "Silje",
    "Thomas",
    "Mary", 
    "Carolyn",
    "Regina",
    "Max",
    "Simon",
    "Patrick",
    "Jenny"]

group_1 = []
group_2 = []
group_3 = []

for i in range(3):
    student = random.choice(students)
    students.remove(student)
    group_1.append(student)

for i in range(3):
    student = random.choice(students)
    students.remove(student)
    group_2.append(student)

for i in range(4):
    student = random.choice(students)
    students.remove(student)
    group_3.append(student)

print(f"Group 1: {group_1}")
print(f"Group 2: {group_2}")
print(f"Group 3: {group_3}")