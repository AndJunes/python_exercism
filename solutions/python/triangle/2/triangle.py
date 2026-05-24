"""Functions to determine triangle types."""


def valid_triangle(sides):
    """Return True if the sides form a valid triangle."""

    side_one, side_two, side_three = sides

    return (
        side_one > 0
        and side_two > 0
        and side_three > 0
        and side_one + side_two >= side_three
        and side_one + side_three >= side_two
        and side_two + side_three >= side_one
    )


def equilateral(sides):
    """Return True if the triangle is equilateral."""

    side_one, side_two, side_three = sides

    return (
        valid_triangle(sides)
        and side_one == side_two == side_three
    )


def isosceles(sides):
    """Return True if the triangle is isosceles."""

    side_one, side_two, side_three = sides

    return (
        valid_triangle(sides)
        and (
            side_one == side_two
            or side_two == side_three
            or side_one == side_three
        )
    )


def scalene(sides):
    """Return True if the triangle is scalene."""

    side_one, side_two, side_three = sides

    return (
        valid_triangle(sides)
        and side_one != side_two
        and side_two != side_three
        and side_one != side_three
    )