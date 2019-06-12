# coding=utf-8
import unittest
from generator_test import (generator_function, fibon, generator, averager, odds, odd_even, odd_even_x)


class GeneratorTests(unittest.TestCase):

    def test_simple_iterator(self):
        for item in generator_function():
            print(item)

    def test_multi_call(self):
        g = generator_function()
        print(g.next())
        print(g.next())
        print(g.next())
        print(g.next())

    def test_fibon(self):
        for x in fibon(1000000):
            print(x)

    def test_generator_no_return(self):
        x = generator()
        next(x)
        # => before
        next(x)
        # => middle
        try:
            next(x)
        except StopIteration:
            pass
        else:
            self.fail("expected a StopIteration")

    def test_averager(self):
        x = averager()
        self.assertEqual(x.send(None), 0)
        self.assertEqual(x.send(1), 1)
        a2 = x.send(2)
        # print(a2)
        self.assertEqual(a2, 1.5)
        self.assertEqual(x.send(3), 2)

    def test_odd(self):
        x = odds(3)
        self.assertEqual(1, next(x))
        try:
            i = next(x)
            self.assertEqual(3, i)
        except StopIteration:
            pass
        else:
            self.fail("expected a StopIteration")

    def test_odd_even(self):
        x = odd_even(6)
        self.checker(x, (1, 3, 5, 0, 2, 4))

    def test_odd_even_x(self):
        x = odd_even_x(6)
        self.checker(x, (1, 3, 5, 0, 2, 4))

    def checker(self, x, r):
        size = len(r)
        for i in range(size):
            a = next(x)
            self.assertEqual(r[i], a)
