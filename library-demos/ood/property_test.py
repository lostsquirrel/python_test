

import inspect
import unittest


class Data:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        self._value

    @value.setter
    def value(self, v):
        self._value = v

    # def naked(self):


class PropertyTest(unittest.TestCase):

    def test_a(self):
        d = Data()
        d.value = 123
        for x in inspect.getmembers(d, lambda a: inspect.isroutine(a)):
            print(x)
        
        for x in inspect.getmembers(d, lambda a:  inspect.isgetsetdescriptor(a)):
            print(x)
        
        print(getattr(d, "value"))
