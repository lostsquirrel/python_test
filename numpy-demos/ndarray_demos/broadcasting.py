# encoding utf-8
import numpy as np
import unittest

start = np.zeros((4,3))

# create a rank 1 ndarray with 3 values
add_rows = np.array([1, 0, 2])
# create an ndarray which is 4 x 1 to broadcast across columns
add_cols = np.array([[0,1,2,3]])
add_cols = add_cols.T

class Broadcasting(unittest.TestCase):

    def test_start(self):
        print(start)

    def test_add_row(self):
        print(add_rows)

    def test_add_row_start(self):
        y = start + add_rows  # add to each row of 'start' using broadcasting
        print(y)

    def test_add_cols(self):
        print(add_cols)

    def test_add_cols_start(self):
        # add to each column of 'start' using broadcasting
        y = start + add_cols
        print(y)

    def test_add_both(self):
        # this will just broadcast in both dimensions
        add_scalar = np.array([1])
        print(start + add_scalar)

    def test_slides(self):
        # create our 3x4 matrix
        arrA = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        print(arrA)
        # create our 4x1 array
        arrB = [0, 1, 0, 2]
        print(arrB)
        # add the two together using broadcasting
        print(arrA + arrB)