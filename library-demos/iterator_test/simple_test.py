# -*- coding: utf-8 -*-
import unittest

from iterator_test import (PowTwo)


class IteratorTests(unittest.TestCase):

    def test_simple_iterator(self):
        my_list = [1, 2, 3, 4]
        it = iter(my_list)
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, it.__next__())
        self.assertEqual(4, it.__next__())
        try:
            next(it)
        except StopIteration:
            pass
        else:
            self.fail('expected a StopIteration ')

    def test_self_defined_iterator(self):
        a = PowTwo(4)
        it = iter(a)
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(4, next(it))
        self.assertEqual(8, next(it))
        self.assertEqual(16, next(it))
        try:
            next(it)
        except StopIteration:
            pass
        else:
            self.fail('expected a StopIteration ')
