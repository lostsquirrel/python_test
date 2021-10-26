import unittest

from sched_test import print_some_times
from utils import print_time


class SchedulerTest(unittest.TestCase):
    def test_print_time(self):
        print_time()
        self.assertTrue(True)

    def test_print_some_times(self):
        print_some_times()

if __name__ == '__main__':
    unittest.main()
