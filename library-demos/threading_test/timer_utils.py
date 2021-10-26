# -*- coding: utf-8 -*-
from threading import Timer


def timer_worker(delay, action, args=None):
    if args is None:
        args = ()

    t = Timer(delay, action, *args)
    t.start()
    print(t.is_alive())
    while not t.is_alive():
        t = Timer(delay, action, *args)

