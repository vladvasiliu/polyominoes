from polyominoes.polyomino import first_polyomino, Polyomino
from polyominoes.transformations import rotate, reflect, normalise


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
        for transformed_polyomino in transformations(polyomino):
            if transformed_polyomino in polyomino_set:
                break
        else:
            polyomino_set.add(transformed_polyomino)
            yield transformed_polyomino


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


def transformations(polyomino):
    orig_container = polyomino.container
    for reflected_container in reflections(orig_container):
        for rotated_container in rotations(reflected_container):
            normalised_container = normalise(rotated_container)
            yield Polyomino(normalised_container)


def reflections(container):
    yield container
    yield reflect(container)


def rotations(container):
    for _ in range(4):
        container = rotate(container)
        yield container

