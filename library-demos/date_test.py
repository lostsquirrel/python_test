import unittest
from datetime import datetime


class DateTest:

    def test_date_to_timestamp(self):
        d = datetime(2005, 7, 14)
        print(d.timestamp())


if __name__ == '__main__':
    unittest.main()
