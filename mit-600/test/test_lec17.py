# encoding: utf-8

import unittest
from lec17 import *


class TestLec17(unittest.TestCase):

    def test_simple(self):
        drunk = Drunk('Homer Simpson')
        for i in range(3):
            f = Field(drunk, Location(0, 0))
            distances = perform_trial(500, f)
            pylab.plot(distances)
        pylab.title('Homer\'s Random Walk')
        pylab.xlabel('Time')
        pylab.ylabel('Distance from Origin')

        # ansQuest(500, 300)
        pylab.show()


