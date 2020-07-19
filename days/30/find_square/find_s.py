import math


def is_square(a, b, c, d):
    # find distance between two different sets of points
    d1 = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    d2 = math.sqrt((c[0] - d[0]) ** 2 + (c[1] - d[1]) ** 2)

    if d1 == d2:
        # To be a square, the distance from A to the other points should be the same.
        b1 = math.sqrt((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2)
        b2 = math.sqrt((a[0] - d[0]) ** 2 + (a[1] - d[1]) ** 2)
        if b1 == b2:
            return True

    return False
