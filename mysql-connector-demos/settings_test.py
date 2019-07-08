# coding=utf-8
import unittest
from settings import (get_mysql_config)
from utils import create_connection


class SettingsTests(unittest.TestCase):

    def test_mysql_config(self):
        mysql_config = get_mysql_config()
        print(mysql_config)
        self.assertEqual('root', mysql_config['user'])

    def test_mysql_connection(self):
        with create_connection(get_mysql_config()) as conn:
            print(conn)
            self.assertIsNotNone(conn)
