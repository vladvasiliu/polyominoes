from copy import deepcopy

from polyominoes.polyomino import empty_container, Polyomino


class TransformationOutOfBoundsException(Exception):
    pass


def translate(polyomino, delta_x, delta_y):
    old_container = polyomino.container
    container_size = len(old_container)
    new_container = empty_container(container_size)

    for src_y in range(container_size):
        for src_x in range(container_size):
            if old_container[src_y][src_x]:
                dst_x = src_x + delta_x
                dst_y = src_y + delta_y

                if dst_x < 0 or dst_x > container_size - 1 or dst_y < 0 or dst_y > container_size - 1:
                    raise TransformationOutOfBoundsException
                new_container[dst_y][dst_x] = 1
    return Polyomino(new_container)


def rotate_90(container):
    old_container = container
    container_size = len(old_container)
    new_container = empty_container(container_size)

    for y in range(container_size):
        for x in range(container_size):
            if old_container[y][x]:
                new_container[x][container_size - 1 - y] = 1

    return new_container


def rotate_180(container):
    old_container = container
    container_size = len(old_container)
    new_container = empty_container(container_size)

    for y in range(container_size):
        for x in range(container_size):
            if old_container[y][x]:
                new_container[container_size - 1 - y][container_size - 1 - x] = 1

    return new_container


def rotate_270(container):
    old_container = container
    container_size = len(old_container)
    new_container = empty_container(container_size)

    for y in range(container_size):
        for x in range(container_size):
            if old_container[y][x]:
                new_container[container_size - 1 - x][y] = 1

    return new_container


def rotate(polyomino, times):
    """one rotation is 90 degrees clockwise
    """
    container = polyomino.container
    times %= 4

    if times == 1:
        return Polyomino(rotate_90(container))
    elif times == 2:
        return Polyomino(rotate_180(container))
    elif times == 3:
        return Polyomino(rotate_270(container))
    else:
        return polyomino


def reflect(polyomino):
    old_container = polyomino.container
    new_container = deepcopy(old_container)

    for line in new_container:
        line.reverse()

    return Polyomino(new_container)
