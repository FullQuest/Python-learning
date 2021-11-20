# MAP Function.
# Example with nums
def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


# Example with strings
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'Even'
    return mystring[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))


# Take number based on some sort of condition defined by function
def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, mynums)))

# Lambda expression
power3 = lambda num: num ** 3
print(power3(3))

print(list(map(lambda num: num ** 3, mynums)))
# analogue with list comprehension
print([numb ** 3 for numb in mynums])

print(list(filter(lambda num: num % 2 == 0, mynums)))
# analogue with list comprehension
print([numb for numb in mynums if numb % 2 == 0])
