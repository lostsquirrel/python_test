# encoding utf-8
import numpy as np
import unittest

x = np.array([[111,112],[121,122]], dtype=np.int)
y = np.array([[211.1,212.1],[221.1,222.1]], dtype=np.float64)

class ArithmeticArrayOperations(unittest.TestCase):

    def test_display(self):
        print(x)
        print()
        print(y)

    def test_add(self):
        # add
        print(x + y)  # The plus sign works
        print()
        print(np.add(x, y))  # so does the numpy function "add"

    def test_subtract(self):
        # subtract
        print(x - y)
        print()
        print(np.subtract(x, y))

    def test_multiply(self):
        # multiply
        print(x * y)
        print()
        print(np.multiply(x, y))

    def test_divide(self):
        # divide
        print(x / y)
        print()
        print(np.divide(x, y))

    def test_square_root(self):
        # square root
        print(np.sqrt(x))

    def test_exponent(self):
        # exponent (e ** x)
        print(np.exp(x))