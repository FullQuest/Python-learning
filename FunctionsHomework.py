# Write a function that computes the volume of a sphere given its radius.
import math


def sphere_volume(rad):
    return (4 / 3) * math.pi * rad ** 3


print(sphere_volume(2))
print("sphere_volume\n")


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    return low <= num <= high


print(ran_check(3, 1, 10))
print("ran_check\n")


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#
# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output :
# No. of Upper case characters : 4
# No. of Lower case Characters : 33


def up_low(inp_string):
    upper_l = 0
    lower_l = 0
    for letter in inp_string:
        if letter.isupper():
            upper_l += 1
        elif letter.islower():
            lower_l += 1

    return (f'No. of Upper case characters : {upper_l}\nNo. of Lower case characters : {lower_l}')


print(up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))
print("up_low\n")


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(lst):
    return list(dict.fromkeys(lst))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
print("unique_list\n")


# Write a Python function to multiply all the numbers in a list.
# Sample List : [1, 2, 3, -4]
# Expected Output : -24

def multiply(numbers):
    multiply_container = 1
    for num in numbers:
        multiply_container *= num

    return multiply_container


print(multiply([1, 2, 3, -4]))
print("multiply\n")


# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(word):
    # check if word len is even. If not then pop middle symbol.
    if len(word) % 2 != 0:
        middle_let = len(word) // 2
        word = ''.join([word[num] for num in range(len(word)) if num != middle_let])

    # split word with even length, reverse second half, and compare both
    word_first_half = word[:len(word) // 2]
    word_second_half_inverted = word[(len(word) // 2)::][::-1]

    return word_first_half in word_second_half_inverted


print(palindrome('helleh'))
print("palindrome\n")

# Hard:
# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
#
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
#
# Hint: You may want to use .replace() method to get rid of spaces.
# Hint: Look at the string module
# Hint: In case you want to use set comparisons

import string


def ispangram(input_str, alphabet=string.ascii_lowercase):

    # loop through all symbols in string and trying to pop that symbol from alphabet.
    # If at the end length of alphabet == 0 then return true (because each symbol used)
    for symb in input_str:
        alphabet = alphabet.replace(symb, '')

    return len(alphabet) == 0


print(ispangram("The quick brown fox jumps over the lazy dog"))
print("ispangram")
