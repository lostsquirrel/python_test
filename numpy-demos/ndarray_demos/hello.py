# encoding utf-8
import unittest
import numpy as np


class Hello(unittest.TestCase):

    def test_numpy_version(self):
        print(np.version.version)

    def test_ndarray(self):
        an_array = np.array([3, 33, 33])
        print(type(an_array))
        print(an_array.shape)
        an_array[1] = 123
        assert an_array[1] == 123
        print(an_array)

    def test_rank_2_array(self):
        a = np.array([[11, 12, 13], [21, 22, 23]])
        print(a)
        print("The shape is {} rows, {} columns: ".format(*a.shape))
        assert a[1, 1] == 22

    def test_zeros(self):
        zeros = np.zeros((2, 2))
        print(type(zeros))
        assert zeros.shape == (2, 2)
        assert zeros[1, 1] == 0

    def test_fill(self):
        a = np.full((2, 2), 9.0)
        assert a.shape == (2, 2)
        assert a[1, 1] == 9

    def test_eye(self):
        a = np.eye(3, 3)
        print(a)

    def test_ones(self):
        a = np.ones((3,3))
        print(a)

    def test_random(self):
        a = np.random.random((3, 3))
        print(a)


if __name__ == '__main__':
    unittest.main()
