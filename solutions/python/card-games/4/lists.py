"""Functions for tracking poker hands and assorted card tasks."""


def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    average_hand = sum(hand) / len(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle_value = hand[len(hand) // 2]

    return average_hand in (first_last_avg, middle_value)

def average_even_is_average_odd(hand):
    even_avg = sum(hand[0::2]) / len(hand[0::2])
    odd_avg = sum(hand[1::2]) / len(hand[1::2])

    return even_avg == odd_avg

def maybe_double_last(hand):
    JACK = 11

    if hand[-1] == JACK:
        hand[-1] = JACK * 2

    return hand