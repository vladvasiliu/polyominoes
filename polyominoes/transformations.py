from operator import itemgetter


def normalise(container):
    """ Translates the polyomino so that all coordinates are positive and minimal.
    """
    delta_x = - min(container, key=itemgetter(0))[0]
    delta_y = - min(container, key=itemgetter(1))[1]

    return translate(container, delta_x, delta_y)


def translate(container, delta_x, delta_y):
    new_container = {(x + delta_x, y + delta_y) for x, y in container}
    return new_container


def rotate(container):
    """ Rotates the container 90 degrees clockwise around (0, 0).
    """
    new_container = {(-y, x) for x, y in container}
    return new_container


def reflect(container):
    new_container = {(-x, y) for x, y in container}
    return new_container


def reflections(container):
    yield container
    yield reflect(container)


def rotations(container):
    for _ in range(4):
        container = rotate(container)
        yield container
