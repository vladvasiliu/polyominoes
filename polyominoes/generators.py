from copy import deepcopy

from polyominoes.helpers import polyomino_in_list
from polyominoes.polyomino import first_polyomino, child_container, first, Polyomino
from polyominoes.transformations import normalise


class CellOutOfBoundsException(Exception):
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

    parent_container = child_container(polyomino.container)
    fist_x, first_y = first(parent_container)
    for _nc in fun(parent_container, fist_x, first_y):
        yield normalise(Polyomino(_nc))


def unique_polyominoes(polyomino_iter):
    """ returns unique polyominoes from an iterable containing polyominoes """
    polyomino_list = set()

    for polyomino in polyomino_iter:
        if not polyomino_in_list(polyomino, polyomino_list):
            polyomino_list.add(polyomino)
            yield polyomino


def polyominoes(order):
    polyomino = first_polyomino()

    polyomino_list = [polyomino]

    if order == 1:
        return polyomino_list

    for _ in range(2, order+1):
        new_list = []
        for polyomino in polyomino_list:
            new_list.extend(children(polyomino))
        polyomino_list = unique_polyominoes(new_list)
    return list(polyomino_list)
