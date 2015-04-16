from copy import deepcopy
from itertools import chain
from operator import itemgetter

__author__ = 'vlad'


def empty_container(size):
    return [[0 for _ in range(size)] for _ in range(size)]


class Polyomino(object):
    """ A polyomino is an array of booleans.
    """
    def __init__(self, container):
        self.container = container
        # self.max_order = int(len(container)/2)
        self.max_order = len(container)

    def __repr__(self):
        result = ''
        for x in self.container:
            for y in x:
                result += 'X' if y else '.'
            result += '\n'
        return result

    def __eq__(self, other):
        try:
            return self.container == other.container
        except AttributeError:
            return False

    @property
    def order(self):
        return sum(chain.from_iterable(self.container))

    @property
    def is_full(self):
        return self.order == self.max_order


class PolyominoIsFullException(Exception):
    pass


class PolyominoNotEmptyException(Exception):
    pass


class CellOutOfBoundsException(Exception):
    pass


class EmptyContainerException(Exception):
    pass


def child_container(container):
    order = len(container)

    new_container = deepcopy(container)

    if max(container[0]):
        insert_pos = 0
    else:
        insert_pos = order
    new_container.insert(insert_pos, [0 for _ in range(order)])

    if max([itemgetter(0)(l) for l in container]):
        insert_pos = 0
    else:
        insert_pos = order

    for line in new_container:
        line.insert(insert_pos, 0)

    return new_container

def first(container):
    order = len(container)
    for y in range(order):
        for x in range(order):
            if container[y][x]:
                return x, y
    raise EmptyContainerException


def traverse_polyomino(polyomino):
    container = polyomino.container
    _x, _y = first(container)

    yield _x, _y

    visited = [(_x, _y)]

    def fun(container, x, y):
        for _x, _y in neighbours(container, x, y):
            if (_x, _y) not in visited and container[_y][_x]:
                visited.append((_x, _y))
                yield _x, _y
                yield from fun(container, _x, _y)
    yield from fun(container, _x, _y)


def first_polyomino():
    polyomino = Polyomino(empty_container(1))

    polyomino.container[0][0] = 1

    return polyomino
