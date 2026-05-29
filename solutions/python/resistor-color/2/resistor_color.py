"""Resistor color band encoding helper."""

def color_code(color):
    """Look up the numerical value associated with a particular color band."""
    for index, item in enumerate(colors()):
        if item == color:
            return index
    return None 


def colors():
    """List the different band colors."""
    color_list = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white",
    ]
    return color_list