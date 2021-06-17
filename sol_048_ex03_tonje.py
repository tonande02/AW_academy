# A FizzBuzz program
# The program counts out the numbers from 1-100, but if the number is divisible
# by 3 it instead prints 'Fizz', if it is divisible by 5 it prints 'Buzz', and
# if the number is divisible by both 3 and 5 it prints 'FizzBuzz'


# the fizz_buzz function
def fizz_buzz(nr):
    if nr % 5 == 0 and nr % 3 == 0:
        return 'FizzBuzz'
    elif nr % 5 == 0:
        return 'Buzz'
    elif nr % 3 == 0:
        return 'Fizz'
    else:
        return nr

# calling the function 100 times
for i in range(1,101):
    print(f"{fizz_buzz(i)}", end=", ")