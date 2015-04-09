import datetime
import sys

from polyominoes.polyomino import polyominoes
from polyominoes.transformations import transformations


def count_polyominoes(order):
    polyomino_list = list()

    for polyomino in polyominoes(order):
        for transformed_polyomino in transformations(polyomino):
            if transformed_polyomino in polyomino_list:
                break
        else:
            polyomino_list.append(polyomino)
    return len(polyomino_list)


# MAX_ORDER = int(sys.argv[1])
# for current_order in range(2, MAX_ORDER+1):
current_order = int(sys.argv[1])
START = datetime.datetime.now()
NUM = count_polyominoes(current_order)
DONE = (datetime.datetime.now() - START).total_seconds()
print("order: %s \t count: %s \t time: %ss" % (current_order, NUM, DONE))
