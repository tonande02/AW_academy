def fib(number):
    if number < 0:
        return 0
    elif number == 0:
        return 0
    elif (number == 1) or (number == 2):
        return 1
    else:
        return fib(number-1) + fib(number-2)