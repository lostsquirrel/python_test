import unittest
from threading import Timer

from utils import hello, print_time, logger_print
from threading_test.timer_utils import timer_worker


class TimerTest(unittest.TestCase):
    def test_something(self):
        t = Timer(3.0, hello)
        t.start()

    def test_timer_worker(self):
        import settings
        timer_worker(1, logger_print)


if __name__ == '__main__':
    unittest.main()
