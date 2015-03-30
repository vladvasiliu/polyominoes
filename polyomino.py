__author__ = 'vlad'


class Polyomino(object):
    def __init__(self, container):
        self._container = container

    def __repr__(self):
        result = ''
        for x in self._container:
            for y in x:
                result += 'X' if y else ''
            result += '\n'
        return result
