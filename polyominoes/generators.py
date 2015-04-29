from helpers import contains_polyomino
from polyominoes.polyomino import first_polyomino, Polyomino
from transformations import transformations


def neighbours(x, y):
    yield x+1, y
    yield x-1, y
    yield x, y+1
    yield x, y-1


def children(polyomino):
    """ The children of a polyomino p are all the polyominoes obtained by adding one square to p.
    :type polyomino: Polyomino
    """
    visited = set()
    parent_container = polyomino.container

    for x, y in parent_container:
        for neighbour in neighbours(x, y):
            if neighbour not in visited and neighbour not in parent_container:
                visited.add(neighbour)
                new_container = set(parent_container)
                new_container.add(neighbour)
                yield Polyomino(new_container)


def unique_polyominoes(polyomino_iter):
    """ returns unique polyominoes from an iterable containing polyominoes """
    polyomino_set = set()

    for polyomino in polyomino_iter:
        if not contains_polyomino(polyomino_set, polyomino):
            polyomino_set.add(polyomino)
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
