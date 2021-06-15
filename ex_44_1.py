# A small calculator program

try:
    num_x = float(input("Input first number: "))
    num_y = float(input("Input second number: "))
    operator = input("Operator (sum / sub / mult / div): ").lower()
except:
    print("Invalid input! Numbers must be digits")
    quit()


result = ""

if operator == "sum":
    result = num_x + num_y
elif operator == "sub":
    result = num_x - num_y
elif operator == "mult":
    result = num_x * num_y
elif operator == "div":
    if num_x or num_y == 0:
        print("Division by zero is illegal")
    else:
        result = num_x / num_y
else:
    print("Invalid operator!")


if result:
    print(f"Answer: {result}")



# alternative method - not filled out
# x = 2
# y = 4
# oper = '*'

# print(eval(f'{x} {oper} {y}'))