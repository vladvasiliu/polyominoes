from copy import deepcopy
from itertools import chain

__author__ = 'vlad'


def empty_container(size):
    return [[0 for _ in range(size)] for _ in range(size)]


class Polyomino(object):
    """ A polyomino is an array of booleans.
    """
    def __init__(self, container):
        self.container = container
        self.max_order = int(len(container)/2)

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


def filled_neighbours(container, x, y):
    container_size = int(len(container))

    if x < -container_size or x >= container_size or y < -container_size or y >= container_size:
        raise CellOutOfBoundsException

    if x > -container_size and not container[x-1][y]:
        new_container = deepcopy(container)
        new_container[x-1][y] = 1
        yield new_container
    if y > -container_size and not container[x][y-1]:
        new_container = deepcopy(container)
        new_container[x][y-1] = 1
        yield new_container
    if x < container_size - 1 and not container[x+1][y]:
        new_container = deepcopy(container)
        new_container[x+1][y] = 1
        yield new_container
    if y < container_size - 1 and not container[x][y+1]:
        new_container = deepcopy(container)
        new_container[x][y+1] = 1
        yield new_container


def children(polyomino):
    """
    :type polyomino: Polyomino
    """
    if polyomino.is_full:
        raise PolyominoIsFullException

    order = polyomino.max_order

    for x in range(-order, order):
        for y in range(-order, order):
            if polyomino.container[x][y]:
                for container in filled_neighbours(polyomino.container, x, y):
                    yield Polyomino(container)


def first_polyomino(order):
    polyomino = Polyomino(empty_container(2*order))

    polyomino.container[order][order] = 1

    return polyomino
