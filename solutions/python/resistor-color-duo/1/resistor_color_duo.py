"""Resistor color band duo encoder — converts 2 color bands to a numeric value."""

COLORS = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]

def value(colors):
    """Return the two-digit number encoded by the first two resistor color bands."""
    return COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])