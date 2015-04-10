from polyominoes.polyomino import first_polyomino, fill_polyomino
from polyominoes.transformations import transformations


def polyomino_in_list(polyomino, polyomino_list):
    for transformed_polyomino in transformations(polyomino):
        if transformed_polyomino in polyomino_list:
            return True
    return False


def unique_polyominoes(polyomino_iter):
    """ returns unique polyominoes from an interable containing polyominoes """
    polyomino_list = list()

    for polyomino in polyomino_iter:
        if not polyomino_in_list(polyomino, polyomino_list):
            polyomino_list.append(polyomino)
            yield polyomino


def polyominoes(order):
    polyomino = first_polyomino(order)

    polyomino_list = [polyomino]

    if order == 1:
        return polyomino_list

    for _order in range(2, order+1):
        new_list = []
        for polyomino in polyomino_list:
            new_list.extend(fill_polyomino(polyomino, max_order=_order))
        polyomino_list = unique_polyominoes(new_list)
    return list(polyomino_list)
