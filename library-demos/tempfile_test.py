

import tempfile
import unittest


class TempFileTest(unittest.TestCase):

    def test_dir(self):
        print(tempfile.gettempdir())

    def test_prefix(self):
        print(tempfile.gettempprefix())

    def test_work_on_dir(self):
        with tempfile.TemporaryDirectory() as temp:
            print(temp)
