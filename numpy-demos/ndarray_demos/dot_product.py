# encoding utf-8
import numpy as np
import unittest

x2d = np.array([[1, 1], [1, 1]])
y2d = np.array([[2, 2], [2, 2]])

a1d = np.array([9, 9])
b1d = np.array([10, 10])


class DotProduct(unittest.TestCase):

    def test_dot2d(self):
        # determine the dot product of two matrices
        print(x2d.dot(y2d))
        print()
        print(np.dot(x2d, y2d))

    def test_dot1d(self):
        # determine the inner product of two vectors
        print(a1d.dot(b1d))
        print()
        print(np.dot(a1d, b1d))

    def testdot2d1d(self):
        # dot produce on an array and vector
        print(x2d.dot(a1d))
        print()
        print(np.dot(x2d, a1d))


'''
If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).

If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.

If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.

If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.

If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the 
second-to-last axis of b:

'''
