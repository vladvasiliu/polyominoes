from polyominoes.polyomino import first_polyomino, fill_polyomino
from polyominoes.transformations import transformations, translations


def unique_polyominoes(polyomino_iter):
    """ returns unique polyominoes from an interable containing polyominoes """
    polyomino_list = list()

    for polyomino in polyomino_iter:
        for transformed_polyomino in transformations(polyomino):
            if transformed_polyomino in polyomino_list:
                break
        else:
            polyomino_list.append(polyomino)
            yield polyomino


def polyominoes(order):
    polyomino = first_polyomino(order)

    polyominoes = [polyomino]

    if order == 1:
        return polyominoes

    for o in range(2, order+1):
        new_list = []
        for polyomino in polyominoes:
            new_list.extend(fill_polyomino(polyomino, max_order=o))
        polyominoes = unique_polyominoes(new_list)
    return list(polyominoes)
