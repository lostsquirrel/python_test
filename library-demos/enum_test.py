import unittest
from enum import Enum, auto


class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()


class EnumTest(unittest.TestCase):

    def test_values(self):
        for x in list(Color):
            print(x)

        # for x in Color.values():
        #     print(x)
