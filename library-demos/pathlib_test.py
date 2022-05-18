# -*- coding: UTF-8 -*-

import unittest
from pathlib import Path, PurePath


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

    def test_glob(self):
        p = Path('.')
        for f in p.glob('**/*.py'):
            print(f)

    def test_resolve(self):
        p = Path('/etc')
        q = p / 'init.d' / 'reboot'
        print(q)
        print(q.resolve())

    def test_fspath(self):
        import os
        p = PurePath('/etc')
        print(os.fspath(p))

        
if __name__ == '__main__':
    unittest.main()
