# encoding utf-8

import unittest
import numpy as np

class ArrayIndexingTests(unittest.TestCase):

    def test_slice(self):
        an_array = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
        print(an_array)
        a_slice = an_array[:2, 1:3]
        print(a_slice)

        a_slice[0, 0] = 1000
        assert an_array[0, 1] == 1000


    def test_indexing_slice(self):
        an_array = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
        print(an_array)
        row_rank1 = an_array[1, :]  # Rank 1 view

        print(row_rank1, row_rank1.shape)  # notice only a single []

    def test_indexing_slice_column(self):
        an_array = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
        col_rank1 = an_array[:, 1]
        col_rank2 = an_array[:, 1:2]
        print(col_rank1, col_rank1.shape)  # Rank 1
        print()
        print(col_rank2, col_rank2.shape)  # Rank 2


    def test_indexes(self):
        # Create a new array
        an_array = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]])

        print('Original Array:')
        print(an_array)
        # Create an array of indices
        col_indices = np.array([0, 1, 2, 0])
        print('\nCol indices picked : ', col_indices)

        row_indices = np.arange(4)
        print('\nRows indices picked : ', row_indices)
        # Examine the pairings of row_indices and col_indices.  These are the elements we'll change next.
        for x in zip(row_indices, col_indices, [1, 2, 3, 4]):
            print(x)
        # Change one element from each row using the indices selected
        an_array[row_indices, col_indices] += 100000

        print('\nChanged Array:')
        print(an_array)

        
    def test_zip(self):
        col_indices = np.array([0, 1, 2, 0])
        row_indices = np.arange(4)

        for row, col in zip(row_indices, col_indices):
            print(row, ", ", col)

if __name__ == '__main__':
    unittest.main()
