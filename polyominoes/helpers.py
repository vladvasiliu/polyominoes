from polyominoes.transformations import transformations

__author__ = 'vlad'


def contains_polyomino(polyomino_iter, polyomino):
    for transformed_polyomino in transformations(polyomino):
        if transformed_polyomino in polyomino_iter:
            return True
    return False
