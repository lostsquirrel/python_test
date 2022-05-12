import unittest
from calendar import Calendar

c = Calendar()


class CalendarTest(unittest.TestCase):

    def test_weekdays(self):

        for x in c.iterweekdays():
            print(x)

    def test_monthdates(self):
        dates = c.itermonthdates(2022, 5)
        i = 0
        for x in dates:
            print(x, type(x))
            i += 1
        print(i)

    def test_monthdays(self):
        for x in c.itermonthdates(2022, 5):
            print(x, type(x))
