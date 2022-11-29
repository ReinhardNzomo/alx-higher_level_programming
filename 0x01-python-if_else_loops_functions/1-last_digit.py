#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

'''
convert number to string
number_to_string = repr(n)

access last char in string
last_digit_string = number_to_string[-1]

convert string to int
last_digit = int(last_digit_string)

in short
last_digit = int(repr(number)[-1])
'''

if (number < 0):
    last_digit *= -1
print('Last digit of {} is {} and is '.format(number, last_digit), end ='')
if (last_digit > 5):
    print('greater than 5')
elif (last_digit < 6):
    print('less than 6 and not 0')
else:
    print('0')
