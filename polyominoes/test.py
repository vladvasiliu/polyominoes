from unittest import TestCase
from generators import polyominoes


class TestAll(TestCase):
    def test_n_2(self):
        self.assertEqual(1, len(polyominoes(2)))

    def test_n_3(self):
        self.assertEqual(2, len(polyominoes(3)))

    def test_n_4(self):
        self.assertEqual(5, len(polyominoes(4)))

    def test_n_5(self):
        self.assertEqual(12, len(polyominoes(5)))

    def test_n_6(self):
        self.assertEqual(35, len(polyominoes(6)))

    def test_n_7(self):
        self.assertEqual(108, len(polyominoes(7)))

    def test_n_8(self):
        self.assertEqual(369, len(polyominoes(8)))

    def test_n_9(self):
        self.assertEqual(1285, len(polyominoes(9)))
