from polyomino import empty_container, Polyomino


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

                if dst_x < 0 or dst_x > container_size -1 or dst_y < 0 or dst_y > container_size - 1:
                    raise TransformationOutOfBoundsException
                new_container[dst_y][dst_x] = 1
    return Polyomino(new_container)
