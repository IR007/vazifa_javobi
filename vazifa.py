from random import randrange
from functools import reduce


def user_name(name):
    return name[::-1] + str(randrange(1, 10))


def convert_add(numbers: list):
    return reduce(lambda a, b: int(a) + int(b), numbers)
