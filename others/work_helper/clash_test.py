# -*- coding: utf-8 -*-
import os
import unittest

from others.work_helper.clash import process_sub, process_config, create_yaml


class Test(unittest.TestCase):

    def test_read(self):
        pass

    def test_process_sub(self):
        p = process_sub()
        print(p)

    def test_process_config(self):
        print(create_yaml(process_config(process_sub())))


if __name__ == '__main__':
    url = os.getenv("SUB_URL")
    unittest.main()
