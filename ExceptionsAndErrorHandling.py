# Error handling and exceptions homework
# Problem 1 Handle the exception thrown by the code below by using try and except blocks.
#
# for i in ['a','b','c']:
#     print(i**2)

print('\nProblem 1. Handle type error in for loop')

for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except TypeError:
        print(f'"{i}" is not a correct value for POW operation (type Error)')

# Handle the exception thrown by the code below by using try
# and except blocks. Then use a finally block to print 'All Done.'
#
# x = 5
# y = 0
#
# z = x/y

print('\nProblem 2. Handle div by 0')

x = 5
y = 0

try:
    print(x/y)
except ZeroDivisionError:
    print('Div by zero detected')


# Write a function that asks for an integer and prints the square of it.
# Use a while loop with a try, except, else block to account for incorrect inputs.

print('\nProblem 3. Handle div by 0')


def ask_int_print_pow():
    while True:
        try:
            input_num = int(input('Please enter the number\n'))
        except ValueError:
            print("Provided input is not a number")
            continue
        else:
            print(input_num**2)
            break


ask_int_print_pow()

print('HW done')