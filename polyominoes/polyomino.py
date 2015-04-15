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


def neighbours(container, x, y):
    """ Get the neighbours of the cell with coordinates (x,y).
    """
    container_size = int(len(container))

    if x < 0 or x >= container_size or y < 0 or y >= container_size:
        raise CellOutOfBoundsException(x, y)

    if x > 0:
        yield x-1, y
    if y > 0:
        yield x, y-1
    if x < container_size - 1:
        yield x+1, y
    if y < container_size - 1:
        yield x, y+1


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
    else:
        raise EmptyContainerException


def children(polyomino):
    """ The children of a polyomino p are all the polyominoes obtained by adding one square to p.
    :type polyomino: Polyomino
    """
    visited = []

    def fun(container, x, y):
        for new_x, new_y in neighbours(container, x, y):
            if (new_x, new_y) in visited:
                continue
            else:
                visited.append((new_x, new_y))

            if container[new_y][new_x]:
                yield from fun(container, new_x, new_y)
            else:
                new_container = deepcopy(container)
                new_container[new_y][new_x] = 1
                yield new_container

    _cc = child_container(polyomino.container)
    _x, _y = first(_cc)
    for _nc in fun(_cc, _x, _y):
        yield Polyomino(_nc)


def first_polyomino(order):
    polyomino = Polyomino(empty_container(1))

    polyomino.container[0][0] = 1

    return polyomino
