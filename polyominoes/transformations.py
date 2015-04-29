from operator import itemgetter


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

    min_x = min(container, key=itemgetter(0))[0]
    min_y = min(container, key=itemgetter(1))[1]

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
    new_container = {(-y, x) for x, y in old_container}
    polyomino.container = new_container
    return polyomino


def reflect(polyomino):
    old_container = polyomino.container
    new_container = {(-x, y) for x, y in old_container}
    polyomino.container = new_container
    return polyomino
