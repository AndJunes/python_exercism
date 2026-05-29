"""Resistor color band trio encoder — converts 3 color bands to a resistance value."""

COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]

def label(colors):
    """Return the resistance value with an appropriate metric prefix.

    :param colors: list - sequence of 3 color names.
    :return: str - the resistance in the format "<value> <prefix>ohms".
    """

    main_value = COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])

    resistance = main_value * 10 ** COLORS.index(colors[2])

    if resistance >= 1_000_000_000:
        return f"{resistance // 1_000_000_000} gigaohms"
    if resistance >= 1_000_000:
        return f"{resistance // 1_000_000} megaohms"
    if resistance >= 1000:
        return f"{resistance // 1000} kiloohms"
    return f"{resistance} ohms"