import unittest


class A:
    pass


class B(A):
    pass


a = A()
b = B()


class ReflectionTest(unittest.TestCase):

    def test_type(self):
        cases = (
            (1, int),
            (1.0, float),
            (int, type),
            (a, A),
            (b, B),
        )
        for case in cases:
            obj, _type = case
            self.assertEqual(type(obj), _type)

    def test_is(self):
        cases = (
            (1, int),
            (int, type),
            (a, A),
            (b, B),
            (b, A, False)
        )
        for case in cases:

            if len(case) == 3:
                obj, _type, _ = case
                self.assertFalse(type(obj) is _type)
            else:
                obj, _type = case
                self.assertTrue(type(obj) is _type)

    def test_isinstance(self):
        cases = (
            (1, int),
            (int, type),
            (a, A),
            (b, B),
            (b, A)
        )
        for case in cases:
            obj, _type = case
            self.assertTrue(isinstance(obj, _type))
