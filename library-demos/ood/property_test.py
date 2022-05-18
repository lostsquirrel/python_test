

import inspect
import unittest


class Data:

    def __init__(self):
        self._x = None

    @property
    def x(self):
        self._x

    @x.setter
    def x(self, v):
        self._x = v

    # def naked(self):


class PropertyTest(unittest.TestCase):

    def test_a(self):
        d = Data()
        d.x = 123
        for x in inspect.getmembers(d, lambda a: inspect.isroutine(a)):
            print(x)

        print(getattr(d, "x"))

    def test_all(self):
        d = Data()
        d.x = 123
        for x in inspect.getmembers(d, lambda a: True):
            print(x)

    def test_method(self):
        d = Data()
        d.x = 123
        for x in inspect.getmembers(d, lambda a: inspect.isfunction(a)):
            print(x)
