def two_consecutive(a, b, c):
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    return abs(a - b) == 1 or abs(b - c) == 1 or abs(c - a) == 1
