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


order = int(sys.argv[1])
start = datetime.datetime.now()
num = count_polyominoes(order)
done = (datetime.datetime.now() - start).total_seconds()
print("order: %s \t count: %s \t time: %ss" % (order, num, done))
