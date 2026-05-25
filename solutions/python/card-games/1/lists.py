"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers."""
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers."""
    rounds_1.extend(rounds_2)
    return rounds_1

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number."""
    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the list."""
    return (sum(hand)/len(hand))

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average."""
    average_first_last = (hand[0] + hand[-1]) / 2
    middle = hand[len(hand)//2]
    average_hand = sum(hand) / len(hand)
    return (average_first_last == average_hand) or (middle == average_hand)

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values)."""
    return ((sum(hand[0::2])/ len(hand[0::2])) == (sum(hand[1::2])/ len(hand[1::2])))

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2."""
    for x in hand:
        if hand[-1] == 11:
            hand[-1] = (11 * 2)
    return hand