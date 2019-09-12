#!/bin/python3

import unittest
from error import error
import Matrix as mx

class ErrorTest(unittest.TestCase):
    """Unittests for error handling"""

    def test_enough_arg(self):
        self.assertEqual(error([]), 84)
        self.assertEqual(error(["SIN"]), 84)
        self.assertEqual(error(["SIN", "1"]), 0)

    def test_matrix_square(self):
        self.assertEqual(error(["EXP", "1", "2"]), 84)
        self.assertEqual(error(["EXP", "1", "2", "3", "4", "5"]), 84)
        self.assertEqual(error(["EXP", "1", "2", "3", "4"]), 0)

    def test_valid_function(self):
        self.assertEqual(error(["ABC", "1"]), 84)
        self.assertEqual(error(["SI", "1"]), 84)
        self.assertEqual(error(["EXP", "1"]), 0)

    def test_type(self):
        self.assertEqual(error(["EXP", "a"]), 84)
        self.assertEqual(error(["EXP", "10.7"]), 84)
        self.assertEqual(error(["EXP", "1", "2", "3", "4"]), 0)

class MatrixTest(unittest.TestCase):
    """Unittest for Matrix class"""

    def setUp(self):
        self.test2 = mx.SquareMatrix(["1", "2", "3", "4"])
        self.test3 = mx.SquareMatrix(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    def test_init(self):
        self.assertEqual(self.test2.size, 2)
        self.assertEqual(self.test2.lines, [[1.0, 2.0], [3.0, 4.0]])

    def test_get_identity(self):
        id_test = self.test3.get_identity().lines
        id_brut = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(id_test , id_brut)

    def test_add(self):
        self.test2 += self.test2
        self.assertEqual(self.test2.lines, [[2, 4], [6, 8]])
        addition = self.test2 + self.test2
        self.assertEqual(addition.lines, [[4, 8], [12, 16]])
