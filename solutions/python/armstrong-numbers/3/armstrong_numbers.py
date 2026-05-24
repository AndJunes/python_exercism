"""Check if a number is an Armstrong number."""


def is_armstrong_number(number):
    """Return True if the number is an Armstrong number."""

    digitals = len(str(number))
    total = 0

    for digit in str(number):
        total += int(digit) ** digitals

    return total == number