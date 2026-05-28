"""Score a single toss of a Darts game based on (x, y) coordinates."""
def score(x, y):
    """Calculate the points scored by a dart landing at (x, y)."""
    distance = (x ** 2 + y ** 2) ** 0.5
    if  0 <= distance <= 1:
        return 10
    if 1 < distance <= 5:
        return 5
    if 5 < distance <= 10:
        return 1
    return 0