# -*- coding: utf-8 -*-

import sched
import time

from utils import print_time

s = sched.scheduler(time.time, time.sleep)


def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 3, print_time, argument=('3',))
    s.enter(5, 4, print_time, argument=('4',))
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.enter(5, 50, print_time, argument=('50',))
    s.enter(5, 40, print_time, argument=('40',))
    s.run()
    print(time.time())
