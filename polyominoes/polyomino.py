from copy import deepcopy
from itertools import chain, product
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

    def __hash__(self):
        return hash(str(self.container))

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


class EmptyContainerException(Exception):
    pass


def child_container(container):
    order = len(container)

    new_container = deepcopy(container)

    insert_pos = 1 - max(container[0]) and order
    new_container.insert(insert_pos, [0 for _ in range(order)])

    insert_pos = 1 - max([itemgetter(0)(l) for l in container]) and order

    for line in new_container:
        line.insert(insert_pos, 0)

    return new_container


def first(container):
    order = len(container)
    for x, y in product(range(order), repeat=2):
        if container[y][x]:
            return x, y
    raise EmptyContainerException


def first_polyomino():
    polyomino = Polyomino(empty_container(1))

    polyomino.container[0][0] = 1

    return polyomino
