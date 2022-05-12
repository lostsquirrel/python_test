import unittest
from dataclasses import asdict, dataclass


@dataclass
class A:
    a: int
    b: str


class DataClassTest(unittest.TestCase):

    def test_init(self):
        a = A(1, "a")
        print(a)
        a2 = A(a=2, b="2")
        print(a2)
        print(asdict(a2))
