from copy import deepcopy


def neighbours(x, y):
    for new_x, new_y in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
        if new_y > 0 or new_x > 0 and new_y == 0:
            yield new_x, new_y


class IllegalSquareException(Exception):
    pass


class State(object):
    def __init__(self):
        super(State, self).__init__()
        self.numbered_squares = {0: (0, 0)}
        self.used_squares = set()

    def __repr__(self):
        grid = self.grid
        grid.reverse()
        result = ''
        for y in grid:
            for x in y:
                result += "X" if x else "."
            result += '\n'
        return result

    @property
    def polyomino(self):
        return set(self.numbered_squares[x] for x in self.used_squares)

    @property
    def grid(self):
        order = len(self.used_squares)
        grid = []
        for y in range(order):
            line = []
            for x in range(order):
                if (x, y) in self.polyomino:
                    line.append(1)
                else:
                    line.append(0)
            grid.append(line)
        return grid

    @property
    def free_squares(self):
        last_num = max(self.used_squares, default=-1)
        return [num for num in self.numbered_squares if num > last_num and num not in self.used_squares]

    def _add_square(self, square_number):
        if square_number not in self.free_squares:
            raise IllegalSquareException("requested: %s, available: %s" % (square_number, self.free_squares))

        self.used_squares.add(square_number)
        next_square_num = max(self.numbered_squares.keys()) + 1
        for neighbour in neighbours(*self.numbered_squares[square_number]):
            if neighbour not in self.numbered_squares.values():
                self.numbered_squares[next_square_num] = neighbour
                next_square_num += 1

    @property
    def children(self):
        for free_square in self.free_squares:
            new_state = deepcopy(self)
            new_state._add_square(free_square)
            yield new_state

    @classmethod
    def generate(cls, order):
        states = [cls()]
        for _ in range (order):
            children = []
            for state in states:
                children.extend(state.children)
            states = children
        return states
