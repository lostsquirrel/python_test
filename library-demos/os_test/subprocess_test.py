from stringprep import map_table_b2
import subprocess

import unittest


class SubprocessTest(unittest.TestCase):

    def test_ls(self):
        result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
        for line in result.stdout.decode().split("\n"):
            print(line)

    def test_ls2(self):
        result = subprocess.run(
            ['ls', '-l'], capture_output=True, text=True).stdout
        print(result)

    def test_tail(self):
        result = subprocess.run(
            ['tail', '-f', "/tmp/test"], capture_output=True, text=True).stdout
        print(result)
        