# -*- coding:utf-8 -*-
'''
Created on 2015-2-5

@author: lisong
'''

import unittest
import datetime as dt
from datetime import date, datetime, timedelta
import time
'''

'''


def str2date(date_str, pattern="%Y-%m-%d"):
    return datetime.strptime(date_str, pattern).date()


def str2datetime(date_str, pattern="%Y-%m-%d"):
    return datetime.strptime(date_str, pattern)


class DateTimeTest(unittest.TestCase):

    def test_(self):
        d1 = str2datetime('2000-10-05')
        print(d1, type(d1))
        d2 = str2date('2000-10-05')
        print(d2, type(d2))

    def test_datetime_time(self):
        print(datetime.now().timestamp())
        print(time.time())

    def test_year_month_date(self):
        d = datetime.now()
        print(d.year, d.month, d.day)

    def test_range(self):
        a = datetime(2022, 5, 15)
        b = datetime(2022, 5, 15)
        print(b - a)

    def test_range2(self):
        a = datetime(2022, 5, 15)
        b = datetime(2022, 5, 20)
        delta = b - a
        print(delta.days)
        for d in range(delta.days):
            print(a + timedelta(days=d))
