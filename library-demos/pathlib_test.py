# -*- coding: UTF-8 -*-

import unittest
from pathlib import Path


class PathLibTests(unittest.TestCase):

    def test_parent(self):
        p = Path(__file__)
        print(p, p.parent)
        self.assertTrue(str(p).startswith(str(p.parent)))

    def test_path(self):
        print(Path(__file__).parent.resolve())
        self.assertTrue(True)

    def test_cwd_path(self):
        cwd = Path().resolve()
        print(cwd)
        print(type(cwd))
        self.assertTrue(str(cwd).index("library-demos") != -1)


if __name__ == '__main__':
    unittest.main()
