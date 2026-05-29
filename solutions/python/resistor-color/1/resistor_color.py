"""you need to know two things about them: Each resistor has a resistance value. Resistors are small - so small in fact that if you printed the resistance value on them, it would be hard to read."""
def color_code(color):
    """to look up the numerical value associated with a particular color band"""
    for index, item in enumerate(colors()):
        if item == color:
            return index

def colors():
    """to list the different band colors"""
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return colors