# -*- coding:utf-8 -*-
'''
Created on 2015-2-5

@author: lisong
'''

import datetime as dt
from datetime import date, datetime
import time
'''

'''
def str2date(date_str, pattern = "%Y-%m-%d"):
    return datetime.strptime(date_str, pattern).date()

def str2datetime(date_str, pattern = "%Y-%m-%d"):
    return datetime.strptime(date_str, pattern)

import unittest


class DateTimeTest(unittest.TestCase):

    def test_(self):
        d1 = str2datetime('2000-10-05')
        print(d1, type(d1))
        d2 = str2date('2000-10-05')
        print(d2, type(d2))

    def test_datetime_time(self):
        print(datetime.now().timestamp())
        print(time.time())
