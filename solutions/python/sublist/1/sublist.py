"""Sublist exercism"""

SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """Classify the relationship between two lists.

    :param list_one: list - the first list.
    :param list_two: list - the second list.
    :return: int - one of SUBLIST, SUPERLIST, EQUAL, or UNEQUAL.
    """
    if list_one == list_two:
        return EQUAL
    if _contains(list_two, list_one):
        return SUBLIST
    if _contains(list_one, list_two):
        return SUPERLIST
    return UNEQUAL


def _contains(larger, smaller):
    """Check if `smaller` appears as a contiguous subsequence in `larger`."""
    size = len(smaller)
    if size == 0:
        return True   # lista vacía está "contenida" en cualquier lista
    return any(
        larger[i:i + size] == smaller
        for i in range(len(larger) - size + 1)
    )