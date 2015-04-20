from unittest import TestCase

from polyominoes.polyomino import Polyomino
from polyominoes.transformations import reflect, rotate


class TestReflect(TestCase):
    def test_all_corners_full(self):
        polyomino = Polyomino([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        reflected_polyomino = reflect(polyomino)
        expected_polyomino = Polyomino([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        self.assertEqual(reflected_polyomino, expected_polyomino)

    def test_diagonal(self):
        polyomino = Polyomino([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        reflected_polyomino = reflect(polyomino)
        expected_polyomino = Polyomino([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        self.assertEqual(reflected_polyomino, expected_polyomino)

    def test_center_only(self):
        polyomino = Polyomino([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        reflected_polyomino = reflect(polyomino)
        expected_polyomino = Polyomino([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        self.assertEqual(reflected_polyomino, expected_polyomino)


class TestRotate(TestCase):
    def test_all_corners_full(self):
        polyomino = Polyomino([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        rotate_polyomino = rotate(polyomino)
        expected_polyomino = Polyomino([[1, 0, 1], [0, 0, 0], [1, 0, 1]])
        self.assertEqual(rotate_polyomino, expected_polyomino)

    def test_diagonal(self):
        polyomino = Polyomino([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        rotated_polyomino = rotate(polyomino)
        expected_polyomino = Polyomino([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
        self.assertEqual(rotated_polyomino, expected_polyomino)

    def test_upper_line(self):
        polyomino = Polyomino([[1, 1, 1, 1], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        rotated_polyomino = rotate(polyomino)
        expected_polyomino = Polyomino([[0, 1, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]])
        self.assertEqual(rotated_polyomino, expected_polyomino)
