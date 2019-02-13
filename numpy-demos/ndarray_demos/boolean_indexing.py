# encoding utf-8
import numpy as np
import unittest

class BooleanIndexing(unittest.TestCase):

    def test_change_elements(self):
        # create a 3x2 array
        an_array = np.array([[11, 12], [21, 22], [31, 32]])
        print(an_array)
        # create a filter which will be boolean values for whether each element meets this condition
        filter = (an_array > 15)
        print(filter)
        # we can now select just those elements which meet that criteria
        print(an_array[filter])

        # For short, we could have just used the approach below without the need for the separate filter array.
        print(an_array[(an_array % 2 == 0)])

        an_array[an_array % 2 == 0] += 100
        print(an_array)
