# A small calculator program

## accepting and checking input
try:
    num_x = float(input("Input first number: "))
    num_y = float(input("Input second number: "))
except:
    print("Invalid input! Numbers must be digits")
    quit()


## calculation method 1 - using if-statements
# operator = input("Operator (sum / sub / mult / div): ").lower()
# result = ""

# if operator == "sum":
#     result = num_x + num_y
# elif operator == "sub":
#     result = num_x - num_y
# elif operator == "mult":
#     result = num_x * num_y
# elif operator == "div":
#     if num_x or num_y == 0:
#         print("Division by zero is illegal")
#     else:
#         result = num_x / num_y
# else:
#     print("Invalid operator!")


# if result:
#     print(f"Answer: {result}")



## method 2 - uing eval
operator = input("Operator (+ - * /): ")
operator_list = ['+', '-', '/', '*']

if operator in operator_list:
    if operator == '/' and (num_x == 0 or num_y == 0):
        print("Invalid input!")
    else:
        print(eval(f'{num_x} {operator} {num_y}'))
else:
    print("Invalid operator!")