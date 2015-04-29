from copy import deepcopy

from polyominoes.transformations import normalise


__author__ = 'vlad'


class Polyomino(object):
    """ A polyomino is an array of booleans.
    """
    def __init__(self, container):
        self.max_order = len(container)
        self.container = container

    def __repr__(self):
        result = '\n'

        normalised_self = normalise(deepcopy(self))
        for y in range(self.max_order):
            for x in range(self.max_order):
                result += 'X' if (x, y) in normalised_self.container else '.'
            result += '\n'
        return result

    def __eq__(self, other):
        try:
            return self.container == other.container
        except AttributeError:
            return False

    def __hash__(self):
        return hash(str(self.container))


class PolyominoIsFullException(Exception):
    pass


class PolyominoNotEmptyException(Exception):
    pass


class EmptyContainerException(Exception):
    pass


def first_polyomino():
    return Polyomino({(0, 0)})
