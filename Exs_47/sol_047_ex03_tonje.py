def simple_calc(x, y, operator):
    operator_list = ['+', '-', '/', '*']
    result = None

    if operator in operator_list:
        if operator == '/' and (num_x == 0 or num_y == 0):
            print("Invalid input!")
        else:
            result = eval(f'{num_x} {operator} {num_y}')
    else:
        print("Invalid operator!")
        return None

    return result


## accepting and checking input
try:
    num_x = float(input("Input first number: "))
    num_y = float(input("Input second number: "))
    oper = input("Input operator (+ - * /): ")
except:
    print("Invalid input! Numbers must be digits, and operator must be + - / *")
    quit()


print(simple_calc(num_x, num_y, oper))