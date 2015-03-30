from copy import deepcopy
from itertools import chain

__author__ = 'vlad'


class Polyomino(object):
    """ A polyomino is an array of bools.
    """
    def __init__(self, container):
        self.container = container
        order = len(container)
        for line in container:
            if not line:
                line += [0] * order

    def __repr__(self):
        result = ''
        for x in self.container:
            for y in x:
                result += 'X' if y else '.'
            result += '\n'
        return result

    @property
    def order(self):
        return sum(chain.from_iterable(self.container))

    @property
    def max_order(self):
        return len(self.container)

    @property
    def is_valid(self):
        return self.order == self.max_order

    @property
    def can_increase_order(self):
        return self.order < self.max_order


class PolyominoIsCompleteException(Exception):
    pass


class PolyominoNotEmptyException(Exception):
    pass


def bootstrap(polyomino):
    """
    :type polyomino: Polyomino
    """
    if polyomino.max_order == 0:
        raise PolyominoIsCompleteException
    if polyomino.order > 0:
        raise PolyominoNotEmptyException

    max_order = polyomino.max_order
    container = polyomino.container
    for x in range(max_order):
        for y in range(max_order):
            new_container = deepcopy(container)
            new_container[x][y] = 1
            yield Polyomino(new_container)


def increase_order(polyomino):
    """ supposes the polyomino's order can be increased
    :type polyomino: Polyomino
    """
    if not polyomino.can_increase_order:
        raise PolyominoIsCompleteException()

    max_order = polyomino.max_order
    container = polyomino.container
    for x in range(max_order):
        for y in range(max_order):
            if container[x][y]:
                if x > 0 and not container[x-1][y]:
                    new_container = deepcopy(container)
                    new_container[x-1][y] = 1
                    yield Polyomino(new_container)
                if y > 0 and not container[x][y-1]:
                    new_container = deepcopy(container)
                    new_container[x][y-1] = 1
                    yield Polyomino(new_container)
                if x < max_order - 1 and not container[x+1][y]:
                    new_container = deepcopy(container)
                    new_container[x+1][y] = 1
                    yield Polyomino(new_container)
                if y < max_order - 1 and not container[x][y+1]:
                    new_container = deepcopy(container)
                    new_container[x][y+1] = 1
                    yield Polyomino(new_container)
