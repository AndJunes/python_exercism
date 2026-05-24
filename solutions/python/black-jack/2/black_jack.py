"""Functions used in a blackjack game."""


def value_of_card(card):
    """Return the numerical value of the card."""

    if card == "A":
        return 1

    if card in {"J", "Q", "K"}:
        return 10

    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value."""

    if value_of_card(card_one) > value_of_card(card_two):
        return card_one

    if value_of_card(card_one) < value_of_card(card_two):
        return card_two

    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Return the most advantageous value for an ace."""

    if card_one == "A" or card_two == "A":
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 <= 21:
        return 11

    return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a blackjack."""

    ten_cards = {"10", "J", "Q", "K"}

    return (
        (card_one == "A" and card_two in ten_cards)
        or
        (card_two == "A" and card_one in ten_cards)
    )


def can_split_pairs(card_one, card_two):
    """Determine if the hand can be split."""

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if the hand can be doubled down."""

    total = value_of_card(card_one) + value_of_card(card_two)

    return total in {9, 10, 11}
