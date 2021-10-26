# -*- coding: utf-8 -*-
import logging
import time


def hello():
    print("hello, world")


def print_time(a='default'):
    print("From print_time", time.time(), a)


def logger_print(msg="default"):
    logging.debug(msg)
