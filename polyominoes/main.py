import datetime
import sys

from polyominoes.generators import polyominoes


# MAX_ORDER = int(sys.argv[1])
# for current_order in range(2, MAX_ORDER+1):
CURRENT_ORDER = int(sys.argv[1])
START = datetime.datetime.now()
NUM = len(list(polyominoes(CURRENT_ORDER)))
DONE = (datetime.datetime.now() - START).total_seconds()
print("order: %s \t count: %s \t time: %ss" % (CURRENT_ORDER, NUM, DONE))
