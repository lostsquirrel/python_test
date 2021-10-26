# -*- coding: utf-8 -*-
import unittest
from struct import (pack, unpack, calcsize)


class StructTests(unittest.TestCase):


    def test_simple_integer_pack_unpack(self):
        format_xx = '=hhl'
        bb = pack(format_xx, 1, 2, 3)
        print(bb)
        print(unpack(format_xx, bb))
        print(calcsize(format_xx))


    def test_combine_unpack(self):
        record = b'raymond   \x32\x12\x08\x01\x08'
        print(unpack('<10sHHb', record))