# Testing lists

# a)
students = ['Tonje', 'Susan', 'Fredrik', 'Alexis', 'Audun']
print(students)

# b)
print(students[2])

# c)
print(students[2][0])

# d)
students[2] = 'Ole'
print(students)

# e)
students[2] = ['Ole', 'Nordmann']
print(students)

# f)
students.append('Fredrik')
print(students)

# g)
students.insert(4, 'Monty Python')
print(students)

# h)
print(len(students))
students.pop(2)
print(len(students))

# i)
print(students)
print(students.index('Monty Python'))

# j)
print(students[:3])

# k)
students_reverse = students[::-1]
print(students_reverse)

# l)
students_even = students[0: 5: 2]
print(students_even)

# m)
students_odd = students[1:6:2]
print(students_odd)