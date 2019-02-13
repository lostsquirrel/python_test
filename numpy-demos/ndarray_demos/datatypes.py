# encoding utf-8
import numpy as np
import unittest


class DataTypes(unittest.TestCase):

    def test_type_int(self):
        ex1 = np.array([11, 12])  # Python assigns the  data type
        print(ex1.dtype)

    def test_type_float(self):
        ex2 = np.array([11.0, 12.0])  # Python assigns the  data type
        print(ex2.dtype)

    def test_type_assign_int64(self):
        ex3 = np.array([11, 21], dtype=np.int64)  # You can also tell Python the  data type
        print(ex3.dtype)

    def test_type_force_int(self):
        # you can use this to force floats into integers (using floor function)
        ex4 = np.array([11.1, 12.7], dtype=np.int64)
        print(ex4.dtype)
        print()
        print(ex4)

    def test_type_force_float(self):
        # you can use this to force integers into floats if you anticipate
        # the values may change to floats later
        ex5 = np.array([11, 21], dtype=np.float64)
        print(ex5.dtype)
        print()
        print(ex5)