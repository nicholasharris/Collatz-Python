#does the collatz procedure on binary strings

import datetime
import random

def count_ones(s):
    count = 0
    for i in s:
        if i == '1':
            count += 1
    return count

def remove_trailing_zeros(s):
    num_removed = 0
    while s[-1] == '0':  #negative index counts from the right; -1 is the last element of the string
        s = s[:-1]  #remove last character of string
        num_removed += 1
    
    return s, num_removed

def append_one_on_right(s):
    return s + "1"

def last_digit(s):
    if s == "":
        return '0'
    else:
        return s[-1]

def add_binary_strings(s1, s2):
    carry = '0'
    sum = ""

    while s1 != "" or s2 != "" or carry == '1':
        digsum, carry = add_binary_digits(last_digit(s1), last_digit(s2), carry)
        sum = digsum + sum
        s1 = s1[:-1]
        s2 = s2[:-1]

    return sum

def add_binary_digits(d1, d2, carry):
    sum = '0'
    new_carry = '0'

    num_ones = count_ones(d1+d2+carry)

    if num_ones == 0:
        sum = '0'
        new_carry = '0'
    elif num_ones == 1:
        sum = '1'
        new_carry = '0'
    elif num_ones == 2:
        sum = '0'
        new_carry = '1'
    elif num_ones == 3:
        sum = '1'
        new_carry = '1'

    return sum, new_carry

def compare_digits(a,b):
    if a == b:
        return 0
    elif a == '0' and b == '1':
        return -1
    elif a == '1' and b == '0':
        return 1

#compares 2 binary strings to see if a < b
def is_less(a, b):
    if len(a) > len(b):
        return False
    elif len(a) < len(b):
        return True

    for i in range(len(a)):
        if compare_digits(a[i], b[i]) == -1:   # if a < b
            return True
        elif compare_digits(a[i], b[i]) == 1:   # if a > b
            return False

    return False


def collatz_verbose(n):
    steps = 0

    print(f"START: {n}" )

    loop_counter = 0
    while True:
        # remove trailing zeros (equivalent to repeatedly dividing by 2 until n is odd)
        new_n, num_steps = remove_trailing_zeros(n)
        n = new_n
        steps += num_steps

        if loop_counter % 1000 == 0:
            print(f"steps: {steps}, time_stamp: {datetime.datetime.now()()}")
        
        if n == "1":
            print(f"1 reached. Total stopping time: {steps}")
            return steps
        
        # n -> 3n+1  (achieved by adding n + (2n + 1))
        two_n_plus_1 = append_one_on_right(n)
        n = add_binary_strings(n, two_n_plus_1)
        steps += 1

        loop_counter += 1

#gets the total stopping time of collatz(n), i.e. until it reaches 1
def collatz_total(n):
    steps = 0

    while True:
        # remove trailing zeros (equivalent to repeatedly dividing by 2 until n is odd)
        new_n, num_steps = remove_trailing_zeros(n)
        n = new_n
        steps += num_steps
        
        if n == "1":
            return steps
        
        # n -> 3n+1  (achieved by adding n + (2n + 1))
        two_n_plus_1 = append_one_on_right(n)
        n = add_binary_strings(n, two_n_plus_1)
        steps += 1

#performs collatz(n) until a value is reached lower than the initial value
def collatz(n):
    steps = 0
    start = n

    while True:
        # remove trailing zeros (equivalent to repeatedly doing n -> n/2 until n is odd)
        new_n, num_steps = remove_trailing_zeros(n)
        n = new_n
        steps += num_steps

        if is_less(n, start):
            return steps
    
        # n -> 3n+1  (achieved by adding n + (2n + 1))
        two_n_plus_1 = append_one_on_right(n)
        n = add_binary_strings(n, two_n_plus_1)
        steps += 1

def collatz_exhaustive_search_total():
    n = "1"
    length = 1
    iostream = open("collatz_results_total.txt", 'a')

    while True:
        total_stopping_time = collatz_total(n)
        iostream.write(f"{n},{len(n)},{total_stopping_time}\n")

        n = add_binary_strings(n, "1")

        new_length = len(n)
        if new_length > length:
            print(f"reached {new_length} digits (all numbers under 2^{new_length-1} checked). Time stamp: {datetime.datetime.now()}")
            length = new_length

def collatz_exhaustive_search():
    n = "10"
    length = 1
    iostream = open("collatz_results.txt", 'a')

    while True:
        stopping_time = collatz(n)
        iostream.write(f"{n},{len(n)},{stopping_time}\n")

        n = add_binary_strings(n, "1")

        new_length = len(n)
        if new_length > length:
            print(f"reached {new_length} digits (all numbers under 2^{new_length-1} checked). Time stamp: {datetime.datetime.now()}")
            length = new_length


#collatz_exhaustive_search()
collatz_exhaustive_search_total()

'''
big_string = "1"
for i in range(10000):
    if random.random() < 0.5:
        big_string = big_string + '0'
    else:
        big_string = big_string + '1'

collatz_verbose(big_string)
'''