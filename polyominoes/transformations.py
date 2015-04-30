from operator import itemgetter


class TransformationOutOfBoundsException(Exception):
    pass


def transformations(polyomino):
    for reflected_polyomino in reflections(polyomino):
        yield from rotations(reflected_polyomino)


def reflections(polyomino):
    yield polyomino
    yield reflect(polyomino)


def rotations(polyomino):
    for _ in range(4):
        yield rotate(polyomino)


def normalise(polyomino):
    """ Translates the polyomino so that all coordinates are positive and minimal.
    """
    container = polyomino.container

    delta_x = - min(container, key=itemgetter(0))[0]
    delta_y = - min(container, key=itemgetter(1))[1]

    return translate(polyomino, delta_x, delta_y)


def translate(polyomino, delta_x, delta_y):
    old_container = polyomino.container
    new_container = {(x + delta_x, y + delta_y) for x, y in old_container}
    polyomino.container = new_container
    return polyomino


def rotate(polyomino):
    """ Rotates the polyomino 90 degrees clockwise around (0, 0).
    """
    old_container = polyomino.container
    new_container = {(-y, x) for x, y in old_container}
    polyomino.container = new_container
    return polyomino


def reflect(polyomino):
    old_container = polyomino.container
    new_container = {(-x, y) for x, y in old_container}
    polyomino.container = new_container
    return polyomino
