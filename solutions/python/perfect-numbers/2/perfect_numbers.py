"""Determine if a number is perfect, abundant, or deficient based on Nicomachus' """
def classify(number):
    """A perfect number equals the sum of its positive divisors.
    :param number: int - a positive integer
    :return: str - the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    divisors = []
    for item in range(1, number):
        if number % item == 0:
            divisors.append(item)

    aliquot_sum = sum(divisors)

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    return "deficient"