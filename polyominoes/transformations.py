from copy import deepcopy
from itertools import product

from polyominoes.polyomino import Polyomino


class TransformationOutOfBoundsException(Exception):
    pass


def transformations(polyomino):
    for reflected_polyomino in reflections(polyomino):
        yield from rotations(reflected_polyomino)


def reflections(polyomino):
    yield polyomino
    yield reflect(polyomino)


def rotations(polyomino):
    for _ in range(4):
        yield rotate(polyomino)


def normalise(polyomino):
    container = polyomino.container
    order = polyomino.max_order

    min_x, min_y = order, order

    for x, y in product(range(order), repeat=2):
        if container[y][x]:
            min_x = min(min_x, x)
            min_y = min(min_y, y)

    return translate(polyomino, -min_x, -min_y)


def translate(polyomino, delta_x, delta_y):
    if delta_x or delta_y:
        container = polyomino.container
        order = polyomino.max_order
        for dst_x, dst_y in product(range(order + delta_x), range(order + delta_y)):
            src_x = dst_x - delta_x
            src_y = dst_y - delta_y
            if container[src_y][src_x]:
                container[dst_y][dst_x] = 1
                container[src_y][src_x] = 0
    return polyomino


def rotate(polyomino):
    """ Rotates the polyomino 90 degrees clockwise.
        That is: transpose, that reverse each row
    """
    polyomino.container = [list(row) for row in zip(*polyomino.container[::-1])]
    return normalise(polyomino)


def reflect(polyomino):
    old_container = polyomino.container
    new_container = deepcopy(old_container)

    for line in new_container:
        line.reverse()

    return Polyomino(new_container)
