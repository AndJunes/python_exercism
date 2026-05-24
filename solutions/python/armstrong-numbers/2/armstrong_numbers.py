import sys

def is_armstrong_number(number):

    digitals = len(str(number))
    total = 0

    for digit in str(number):
        total += int(digit) ** digitals

    return total == number