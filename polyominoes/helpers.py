from polyominoes.transformations import normalise, transformations

__author__ = 'vlad'


def contains_polyomino(polyomino_iter, polyomino):
    for transformed_polyomino in transformations(polyomino):
        if normalise(transformed_polyomino) in polyomino_iter:
            return True
    return False
