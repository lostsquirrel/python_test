import unittest


class SplitTest(unittest.TestCase):

    def test_max_split(self):
        r = "1.2.3.4".split(".", 1)
        self.assertEqual(len(r), 2)
