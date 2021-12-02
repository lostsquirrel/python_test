import unittest


def make_incrementor(n):
    return lambda x: x + n


def xx(e):
    return e[1]


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]


class TestLambda(unittest.TestCase):

    def test_fun(self):
        f = make_incrementor(42)
        self.assertEqual(42, f(0))

    def test_fun2(self):
        self.assertEqual(3, make_incrementor(1)(2))

    def test_fun3(self):
        pairs.sort(key=lambda pair: pair[1])
        self.assertEqual((4, 'four'), pairs[0])
        print(pairs)

        pairs.sort(key=xx)
        self.assertEqual((4, 'four'), pairs[0])
        print(pairs)
