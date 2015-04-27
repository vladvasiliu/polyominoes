from polyomino import Polyomino


class TransformationOutOfBoundsException(Exception):
    pass


def transformations(polyomino):
    for reflected_polyomino in reflections(polyomino):
        yield from rotations(reflected_polyomino)


def reflections(polyomino):
    yield normalise(polyomino)
    yield normalise(reflect(polyomino))


def rotations(polyomino):
    for _ in range(4):
        yield normalise(rotate(polyomino))


def normalise(polyomino):
    container = polyomino.container
    order = polyomino.max_order

    min_x = order
    min_y = order

    for x, y in container:
        min_x = min(min_x, x)
        min_y = min(min_y, y)

    delta_x = 0 - min_x
    delta_y = 0 - min_y

    return translate(polyomino, delta_x, delta_y)


def translate(polyomino, delta_x, delta_y):
    new_container = polyomino.container
    new_container = {(x + delta_x, y + delta_y) for x, y in new_container}
    polyomino.container = new_container
    return polyomino


def rotate(polyomino):
    """ Rotates the polyomino 90 degrees clockwise.
        That is: transpose, that reverse each row
    """
    old_container = polyomino.container
    order = polyomino.max_order
    new_container = {(order - 1 - y, x) for x, y in old_container}
    polyomino.container = new_container
    return polyomino


def reflect(polyomino):
    old_container = polyomino.container
    order = polyomino.max_order
    new_container = {(order - 1 - x, y) for x, y in old_container}
    polyomino.container = new_container
    return polyomino
