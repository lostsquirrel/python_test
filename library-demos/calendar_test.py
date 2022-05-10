import unittest
from calendar import Calendar

c = Calendar()


class CalendarTest(unittest.TestCase):

    def test_weekdays(self):

        for x in c.iterweekdays():
            print(x)

    def test_monthdates(self):
        for x in c.itermonthdates(2022, 5):
            print(x, type(x))

    def test_monthdays(self):
        for x in c.itermonthdates(2022, 5):
            print(x, type(x))
