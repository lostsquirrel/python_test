# -*- coding: utf-8 -*-

import os
import platform

import unittest


class PathTests(unittest.TestCase):

    def test_file_modify_time(self):
        print(os.path.getmtime(os.path.realpath(__file__)))

    def test_current_file(self):
        print(os.path.realpath(__file__))


if __name__ == '__main__':
    unittest.main()
