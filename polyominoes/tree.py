__author__ = 'vlad'


class Coordinates(tuple):
    def neighbours(self):
        x, y = self
        for new_x, new_y in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
            if new_y > 0 or new_x > 0 and new_y == 0:
                yield Coordinates((new_x, new_y))

    @classmethod
    def origin(cls):
        return cls((0, 0))


class Cell(object):
    def __init__(self, number, coordinates):
        super(Cell, self).__init__()
        self.number = number
        self.coordinates = coordinates

    def __hash__(self):
        return hash(self.coordinates)

    def __eq__(self, other):
        try:
            return self.coordinates == other.coordinates
        except AttributeError:
            return False

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "<%s: %s>" % (self.number, self.coordinates)

    @classmethod
    def origin(cls):
        return cls(0, Coordinates.origin())


class Node(object):
    def __init__(self, parent_node, base_cell):
        super(Node, self).__init__()
        self.parent_node = parent_node
        self.base_cell = base_cell
        self.neighbours, self.max_number = self.__neighbours()
        self.neighbour_coordinates = list(self._all_neighbour_coordinates())

    def __neighbours(self):
        neighbours = []
        if not self.parent_node:
            next_number = 0
            for neighbour in self.base_cell.coordinates.neighbours():
                next_number += 1
                neighbours.append(Cell(next_number, neighbour))
        else:
            next_number = self.parent_node.max_number
            for neighbour in self.base_cell.coordinates.neighbours():
                if neighbour not in self.parent_node.neighbour_coordinates:
                    next_number += 1
                    neighbours.append(Cell(next_number, neighbour))
        return neighbours, next_number

    @classmethod
    def root(cls):
        return cls(None, Cell.origin())

    def _all_neighbour_coordinates(self):
        for neighbour in self.neighbours:
            yield neighbour.coordinates
        if self.parent_node:
            yield from self.parent_node.neighbour_coordinates

    def path(self):
        yield self.base_cell
        if self.parent_node:
            yield from self.parent_node.path()

    def eligible_neighbours(self):
        yield from self.neighbours
        current = self.parent_node
        stop = False
        while current and not stop:
            for neighbour in current.neighbours:
                if neighbour.number > self.base_cell.number:
                    yield neighbour
                else:
                    stop = True
            current = current.parent_node

    def children(self):
        for neighbour in self.eligible_neighbours():
            yield Node(self, neighbour)

    @classmethod
    def order(cls, n):
        root = cls.root()
        result = [root]
        for _ in range(1, n):
            new_result = []
            for r in result:
                new_result.extend(r.children())
            result = new_result
        return result


if __name__ == '__main__':
    from datetime import datetime
    import sys

    order = int(sys.argv[1])
    start = datetime.now()
    count = len(Node.order(order))
    stop = datetime.now()
    total = (stop - start).total_seconds()
    print("order: %s \t count: %s \t time: %s" % (order, count, total))
