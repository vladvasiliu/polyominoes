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


def neighbours(container, x, y):
    """ Get the neighbours of the cell with coordinates (x,y).
    """
    container_size = int(len(container))

    if x < -container_size or x >= container_size or y < -container_size or y >= container_size:
        raise CellOutOfBoundsException

    if x > -container_size:
        yield x-1, y
    if y > -container_size:
        yield x, y-1
    if x < container_size - 1:
        yield x+1, y
    if y < container_size - 1:
        yield x, y+1


def children(polyomino):
    """ The children of a polyomino p are all the polyominoes obtained by adding one square to p.
    :type polyomino: Polyomino
    """
    if polyomino.is_full:
        raise PolyominoIsFullException

    order = polyomino.max_order

    visited = []

    def fun(container, x, y):
        for new_x, new_y in neighbours(container, x, y):
            if (new_x, new_y) in visited:
                continue
            else:
                visited.append((new_x, new_y))

            if container[new_x][new_y]:
                yield from fun(container, new_x, new_y)
            else:
                new_container = deepcopy(container)
                new_container[new_x][new_y] = 1
                yield new_container

    for container in fun(polyomino.container, order, order):
        yield Polyomino(container)


def first_polyomino(order):
    polyomino = Polyomino(empty_container(2*order))

    polyomino.container[order][order] = 1

    return polyomino
