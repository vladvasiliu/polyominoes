from copy import deepcopy
from itertools import chain

__author__ = 'vlad'


def empty_container(order):
    return [[0 for _ in range(order)] for _ in range(order)]


class Polyomino(object):
    """ A polyomino is an array of booleans.
    """
    def __init__(self, container):
        self.container = container
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


def check_bounds(fun):
    def wrap(container, x, y):
        container_size = len(container)
        if x < 0 or x >= container_size or y < 0 or y >= container_size:
            raise CellOutOfBoundsException
        else:
            return fun(container, x, y)
    return wrap


@check_bounds
def filled_neighbours(container, x, y):
    container_side_size = len(container)

    if x > 0 and not container[x-1][y]:
        new_container = deepcopy(container)
        new_container[x-1][y] = 1
        yield new_container
    if y > 0 and not container[x][y-1]:
        new_container = deepcopy(container)
        new_container[x][y-1] = 1
        yield new_container
    if x < container_side_size - 1 and not container[x+1][y]:
        new_container = deepcopy(container)
        new_container[x+1][y] = 1
        yield new_container
    if y < container_side_size - 1 and not container[x][y+1]:
        new_container = deepcopy(container)
        new_container[x][y+1] = 1
        yield new_container


def fill_polyomino(polyomino):
    """
    :type polyomino: Polyomino
    """
    if polyomino.is_full:
        raise PolyominoIsFullException
    max_order = polyomino.max_order
    for x in range(max_order):
        for y in range(max_order):
            if polyomino.container[x][y]:
                for new_container in filled_neighbours(polyomino.container, x, y):
                    new_polyomino = Polyomino(new_container)
                    if new_polyomino.is_full:
                        yield new_polyomino
                    else:
                        yield from fill_polyomino(new_polyomino)


def polyominoes(order):
    polyomino = Polyomino(empty_container(order))

    center = int(order/2)
    polyomino.container[center][center] = 1

    yield from fill_polyomino(polyomino)
