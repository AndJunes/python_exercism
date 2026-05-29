"""Bottle Song reciter — generates verses from a starting bottle count."""

NUMBER_WORDS = ["no", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine", "ten"]


def bottles_phrase(count, capitalize=False):
    """Return phrase like 'ten green bottles' or 'one green bottle'."""
    word = NUMBER_WORDS[count]
    if capitalize:
        word = word.capitalize()
    noun = "bottle" if count == 1 else "bottles"
    return f"{word} green {noun}"


def verse(start):
    """Return the 4 lines of a single verse starting with `start` bottles."""
    current = bottles_phrase(start, capitalize=True)
    remaining = bottles_phrase(start - 1)
    return [
        f"{current} hanging on the wall,",
        f"{current} hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        f"There'll be {remaining} hanging on the wall.",
    ]


def recite(start, take=1):
    """Recite `take` verses of the Bottle Song, starting from `start`.

    :param start: int - number of bottles in the first verse (1-10).
    :param take: int - how many verses to recite (default 1).
    :return: list[str] - the lyrics as a flat list, with "" between verses.
    """
    result = []
    for i in range(take):
        if i > 0:
            result.append("")           # separator between verses
        result.extend(verse(start - i))
    return result