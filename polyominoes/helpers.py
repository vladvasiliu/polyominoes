from polyominoes.transformations import transformations

__author__ = 'vlad'


def polyomino_in_list(polyomino, polyomino_list):
    for transformed_polyomino in transformations(polyomino):
        if transformed_polyomino in polyomino_list:
            return True
    return False
