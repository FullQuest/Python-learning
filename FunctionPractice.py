# WARMUP SECTION:
#
# LESSER OF TWO EVENS:
# Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd
#
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

print('---WARMUP SECTION---\n')


def lesser_of_two_evens(first_num, second_num):
    if first_num % 2 == 0 and second_num % 2 == 0:
        return min([first_num, second_num])
    else:
        return max([first_num, second_num])


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
print('lesser_of_two_evens\n')


# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False


def animal_crackers(name):
    words = name.split(' ')

    if words[0][0] == words[1][0]:
        return True
    return False


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print('animal_crackers\n')


# MAKES TWENTY:
# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
#
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False


def makes_twenty(n1, n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    return False


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
print('makes_twenty\n\n---LEVEL 1 PROBLEMS---\n')


# LEVEL 1 PROBLEMS
#
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

def old_macdonald(name):
    if name == 'macdonald':
        return 'MacDonald'


print(old_macdonald('macdonald'))
print('old_macdonald\n')


# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'


def master_yoda(sentence):
    wordlist = sentence.split(' ')
    reversed_sentence = ' '.join(wordlist[::-1])
    return reversed_sentence


print(master_yoda('I am home'))
print(master_yoda('We are ready'))
print('master_yoda\n')


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True


def almost_there(input_number):
    if abs(100 - input_number) <= 10 or abs(200 - input_number) <= 10:
        return True
    return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print('almost_there\n\n---LEVEL 2 PROBLEMS---\n')


# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False


def has_33(input_array):
    str_input = ''.join([str(int) for int in input_array])
    return '33' in str_input


def has_33_old(input_array):
    cur_val = None
    for number in input_array:
        if number == 3 == cur_val:
            return True
        cur_val = number
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print('has_33\n')


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


def paper_doll(input_string):
    return ''.join([letter * 3 for letter in input_string])


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
print('paper_doll\n')


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21,
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
#
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


def blackjack(n1, n2, n3):
    sum = n1 + n2 + n3
    if sum <= 21:
        return n1 + n2 + n3
    elif sum > 21 and (n1 == 11 or n2 == 11 or n3 == 11):
        if sum - 10 <= 21:
            return sum - 10
    return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
print('blackjack\n')


# SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.
#
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(array):
    num_skip = False
    sum = 0
    for num in array:
        if num == 6:
            num_skip = True
        if num == 9:
            num_skip = False
            continue
        if not num_skip:
            sum += num
    return sum


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print('summer_69\n')


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False


def spy_game_old(input_array, lead_array=[0, 0, 7]):
    # This solution is universal. It's possible to use your own arrays for check order (by default it's 007)

    current_position = 0
    win_position = len(lead_array)

    for number in input_array:
        # each iteration we check if current number is valid.
        # if valid then inc current_position, if equals num that should break cur position then cur_pos = 0.
        # when cur_pos = win_pos function returns True

        awaiting_num = lead_array[current_position]
        ruin_nums = list(dict.fromkeys(lead_array[(current_position + 1):]))

        if number == awaiting_num:
            current_position += 1
        elif number in ruin_nums:
            current_position = 0
        else:
            pass

        if current_position == win_position:
            return True
    return False


# print(spy_game_old([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game_old([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game_old([1, 7, 2, 0, 4, 5, 0]))


# That was fun!!! Huge improvement over older version
def spy_game(input_array, lead_array=[0, 0, 7]):
    # Remove all numbers but 0,7(all unique lead_array nums) from input array and then convert both arrays to strings
    # And then check if input_array_string contains lead_array string

    # convert lead_array values to a string and than array itself to string
    lead_array_str = "".join([str(int) for int in lead_array])

    # remove all numbers but 0,7 from input array and also covert values to a string, and then array itself to string
    cut_input_array_str = "".join([str(x) for x in input_array if x in lead_array])

    # check if string we get after removing 0,7 values contains string lead_array
    return lead_array_str in cut_input_array_str


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
print('spy_game\n')


# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25
# def count_primes(input_number):
def is_prime(num_for_prime_check):
    # no primes under 2 so return False
    if num_for_prime_check < 2:
        return False

    # Loop through all nums in input_num and check if it possible to (%==0) it by any number but 1 and num itself
    for num in range(2, num_for_prime_check):
        if num_for_prime_check % num == 0 and num != num_for_prime_check:
            return False
    return True


def count_primes(num_for_count_primes):
    prime_counter = 0

    # Loop through all nums in input_num and check if it's a prime. It it is then prime_counter += 1
    for num in range(num_for_count_primes + 1):
        if is_prime(num):
            prime_counter += 1
    return prime_counter


# print(is_prime(0))
# print(is_prime(1))
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(5))

print(count_primes(2000))
print(count_primes(100))
print(count_primes(6))
print(count_primes(2))
print('count_primes\n')


# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')
#
# out:   *
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns,
# and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".


def print_big(input_str='no input', drawing_symbol='[', empty_symbol=' ', space='  '):
    input_str = input_str.lower()
    input_str = input_str.replace(' ', 'S')

    # Dictionary with all letters
    letters = {"S": "     \n     \n     \n     \n     ", 'a': "  *  \n * * \n*****\n*   *\n*   *",
               'b': "**** \n*   *\n**** \n*   *\n*****", 'c': "**** \n*    \n*    \n*    \n**** ",
               'd': "**** \n*   *\n*   *\n*   *\n**** ", 'e': "*****\n*    \n**** \n*    \n*****",
               'f': "*****\n*    \n**** \n*    \n*    ", 'g': "*****\n*    \n*  **\n*   *\n*****",
               'h': "*   *\n*   *\n*****\n*   *\n*   *", 'i': " *** \n  *  \n  *  \n  *  \n *** ",
               'j': "    *\n    *\n    *\n*   *\n *** ", 'k': "*   *\n* *  \n**   \n* *  \n*   *",
               'l': "*    \n*    \n*    \n*    \n*****", 'm': "*   *\n** **\n* * *\n*   *\n*   *",
               'n': "*   *\n**  *\n* * *\n*  **\n*   *", 'o': " *** \n*   *\n*   *\n*   *\n *** ",
               'p': "*****\n*   *\n*****\n*    \n*    ", 'q': "*****\n*   *\n*****\n    *\n    *",
               'r': "**** \n*  * \n**** \n* *  \n*  * ", 's': "*****\n*    \n*****\n    *\n*****",
               't': "*****\n  *  \n  *  \n  *  \n  *  ", 'u': "*   *\n*   *\n*   *\n*   *\n *** ",
               'v': "*   *\n*   *\n*   *\n * * \n  *  ", 'w': "* * *\n* * *\n* * *\n* * *\n * * ",
               'x': "*   *\n * * \n  *  \n * * \n*   *", 'y': "*   *\n * * \n  *  \n  *  \n  *  ",
               'z': "*****\n   * \n  *  \n *   \n*****"}

    output = ''
    # Convert to output with dictionary
    for row in range(5):
        for letter in input_str:
            output = output + letters[letter].split('\n')[row] + space
        output = output + '\n'

    return output.replace('*', drawing_symbol).replace(' ', empty_symbol)


print(print_big('Hello world', 'H'))
print(print_big('daydreamer', '@'))
print('print_big\n')

