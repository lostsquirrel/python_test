import unittest
import collections
from unittest.case import TestCase

class CollectionSimpleTest(unittest.TestCase):

    def test_counter(self):
        s = "One two three, one two TREE."
        sx = s.translate(str.maketrans("", "", ",.")).lower().split()
        a = collections.Counter(sx)
        print(a.most_common())


    def test_deaultdict(self):
        di = collections.defaultdict(int)
        print(di)
        self.assertEquals(di["9"], 0)

        dd = collections.defaultdict(list)
        print(dd[1])
        self.assertListEqual(dd[1], [])