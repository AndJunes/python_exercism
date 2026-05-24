def valid_triangle(sides):
    a, b, c = sides

    return (
        a > 0 and b > 0 and c > 0
        and a + b >= c
        and a + c >= b
        and b + c >= a
    )


def equilateral(sides):
    a, b, c = sides

    return valid_triangle(sides) and a == b == c


def isosceles(sides):
    a, b, c = sides

    return valid_triangle(sides) and (
        a == b or b == c or a == c
    )


def scalene(sides):
    a, b, c = sides

    return valid_triangle(sides) and (
        a != b and b != c and a != c
    )