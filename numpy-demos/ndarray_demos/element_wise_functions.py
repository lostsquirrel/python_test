# encoding utf-8
import numpy as np
import unittest


class ElementWiseFunctions(unittest.TestCase):

    def test_max(self):
        # random array
        x = np.random.randn(8)
        print(x)
        # another random array
        y = np.random.randn(8)
        print(y)
        # returns element wise maximum between two arrays
        print(np.maximum(x, y))

    def test_reshape(self):
        # grab values from 0 through 19 in an array
        arr = np.arange(20)
        print(arr)
        # reshape to be a 4 x 5 matrix

        print(arr.reshape(4, 5))

    def test_transpose(self):
        # transpose
        ex1 = np.array([[11, 12], [21, 22]])
        print(ex1.T)

    def test_where_01(self):
        x_1 = np.array([1, 2, 3, 4, 5])

        y_1 = np.array([11, 22, 33, 44, 55])

        filter = np.array([True, False, True, False, True])
        out = np.where(filter, x_1, y_1)
        print(out)

    def test_where_02(self):
        mat = np.random.rand(5, 5)
        print(np.where(mat > 0.5, 1000, -1))

    def test_any_all(self):
        arr_bools = np.array([True, False, True, True, False])
        print(arr_bools.any())
        print(arr_bools.all())

    def test_random_number_generation(self):
        Y = np.random.normal(size=(1, 5))[0]
        print(Y)
        Z = np.random.randint(low=2, high=50, size=4)
        print(Z)
        print(np.random.permutation(Z))  # return a new ordering of elements in Z

        print(np.random.uniform(size=4))  # uniform distribution

        print(np.random.normal(size=4))  # normal distribution

    def test_merging_data_set(self):
        K = np.random.randint(low=2, high=50, size=(2, 2))
        print(K)

        print()
        M = np.random.randint(low=2, high=50, size=(2, 2))
        print(M)
        print(np.vstack((K, M)))

        print(np.hstack((K,M)))

        print(np.concatenate([K, M], axis = 0))

        print(np.concatenate([K, M.T], axis = 1))
