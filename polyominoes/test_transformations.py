from unittest import TestCase

from polyominoes.polyomino import Polyomino
from polyominoes.transformations import reflect, rotate


class TestReflect(TestCase):
    def test_all_corners_full(self):
        polyomino = Polyomino({(0, 0), (0, 3), (3, 0), (3, 3)})
        reflected_polyomino = Polyomino(reflect(polyomino.container))
        expected_polyomino = Polyomino({(0, 0), (0, 3), (-3, 0), (-3, 3)})
        self.assertEqual(reflected_polyomino, expected_polyomino)

    def test_diagonal(self):
        polyomino = Polyomino({(0, 0), (1, 1), (2, 2)})
        reflected_polyomino = Polyomino(reflect(polyomino.container))
        expected_polyomino = Polyomino({(0, 0), (-1, 1), (-2, 2)})
        self.assertEqual(reflected_polyomino, expected_polyomino)

    def test_all_corners_full_around_origin(self):
        polyomino = Polyomino({(-5, -5), (5, 5), (-5, 5), (5, -5)})
        reflected_polyomino = Polyomino(reflect(polyomino.container))
        expected_polyomino = Polyomino({(-5, -5), (5, 5), (-5, 5), (5, -5)})
        self.assertEqual(reflected_polyomino, expected_polyomino)

    def test_L_outside_of_origin(self):
        polyomino = Polyomino({(1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2)})
        reflected_polyomino = Polyomino(reflect(polyomino.container))
        expected_polyomino = Polyomino({(-3, 2), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2)})
        self.assertEqual(reflected_polyomino, expected_polyomino)

    def test_diagonal_across_origin(self):
        polyomino = Polyomino({(0, 0), (-1, 1), (1, -1)})
        reflected_polyomino = Polyomino(reflect(polyomino.container))
        expected_polyomino = Polyomino({(0, 0), (-1, -1), (1, 1)})
        self.assertEqual(reflected_polyomino, expected_polyomino)


class TestRotate(TestCase):
    def test_all_corners_full(self):
        polyomino = Polyomino({(0, 0), (3, 0), (0, 3), (3, 3)})
        rotate_polyomino = Polyomino(rotate(polyomino.container))
        expected_polyomino = Polyomino({(0, 0), (-3, 0), (0, 3), (-3, 3)})
        self.assertEqual(rotate_polyomino, expected_polyomino)

    def test_diagonal(self):
        polyomino = Polyomino({(0, 0), (1, 1), (2, 2)})
        rotated_polyomino = Polyomino(rotate(polyomino.container))
        expected_polyomino = Polyomino({(0, 0), (-1, 1), (-2, 2)})
        self.assertEqual(rotated_polyomino, expected_polyomino)

    def test_upper_line(self):
        polyomino = Polyomino({(0, 0), (1, 0), (2, 0)})
        rotated_polyomino = Polyomino(rotate(polyomino.container))
        expected_polyomino = Polyomino({(0, 0), (0, 1), (0, 2)})
        self.assertEqual(rotated_polyomino, expected_polyomino)

    def test_all_corners_full_around_origin(self):
        polyomino = Polyomino({(-5, -5), (5, 5), (-5, 5), (5, -5)})
        rotated_polyomino = Polyomino(rotate(polyomino.container))
        expected_polyomino = Polyomino({(-5, -5), (5, 5), (-5, 5), (5, -5)})
        self.assertEqual(rotated_polyomino, expected_polyomino)

    def test_L_outside_of_origin(self):
        polyomino = Polyomino({(1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2)})
        rotated_polyomino = Polyomino(rotate(polyomino.container))
        expected_polyomino = Polyomino({(-2, 1), (-2, 2), (-2, 3), (-1, 1), (0, 1), (1, 1), (2, 1)})
        self.assertEqual(rotated_polyomino, expected_polyomino)

    def test_L_around_origin(self):
        polyomino = Polyomino({(-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), (0, 2), (1, 2), (2, 2)})
        rotated_polyomino = Polyomino(rotate(polyomino.container))
        expected_polyomino = Polyomino({(-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -1), (0, -1), (1, -1), (2, -1)})
        self.assertEqual(rotated_polyomino, expected_polyomino)
