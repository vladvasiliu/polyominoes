from polyominoes.transformations import normalise


__author__ = 'vlad'


class Polyomino(object):
    """ A polyomino is a set of coordinates. It's immutable.
    """
    def __init__(self, container):
        self.max_order = len(container)
        self._container = frozenset(container)

    def __repr__(self):
        result = '\n'

        normalised_container = normalise(self.container)
        for y in range(self.max_order):
            for x in range(self.max_order):
                result += 'X' if (x, y) in normalised_container else '.'
            result += '\n'
        return result

    def __eq__(self, other):
        try:
            return self.container == other.container
        except AttributeError:
            return False

    def __hash__(self):
        return hash(self.container)

    @property
    def container(self):
        return self._container


class PolyominoIsFullException(Exception):
    pass


class PolyominoNotEmptyException(Exception):
    pass


class EmptyContainerException(Exception):
    pass


def first_polyomino():
    return Polyomino({(0, 0)})
