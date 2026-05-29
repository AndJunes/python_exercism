"""Diamond shape generator — builds a diamond from 'A' to the given letter."""

def rows(letter):
    """Build a diamond as a list of strings, given the letter at the widest point.

    :param letter: str - a single uppercase letter (A-Z).
    :return: list[str] - rows of the diamond, top to bottom.
    """
    if letter == 'A':
        return ['A']

    target_position = ord(letter) - ord('A')

    top_half = []
    for current_position in range(target_position + 1):
        current_letter = chr(ord('A') + current_position)
        outer_spaces = ' ' * (target_position - current_position)

        if current_position == 0:
            row = outer_spaces + 'A' + outer_spaces
        else:
            inner_spaces = ' ' * (2 * current_position - 1)
            row = outer_spaces + current_letter + inner_spaces + current_letter + outer_spaces

        top_half.append(row)

    bottom_half = list(reversed(top_half[:-1]))

    return top_half + bottom_half