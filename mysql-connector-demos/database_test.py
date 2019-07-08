# coding=utf-8
import unittest
import settings
import utils


class DatabaseTests(unittest.TestCase):
    def setUp(self) -> None:
        config = settings.get_mysql_config()
        self.connection = utils.create_connection(config)
        self.db_name = 'mysql_connector_test'

    def tearDown(self) -> None:
        self.connection.close()

    def test_cursor(self):
        print(self.connection.cursor())

    def test_create_db(self):
        utils.create_database(self.connection, self.db_name)

    def test_show_database(self):
        dbs = utils.show_databases(self.connection)
        print(dbs)
        self.assertTrue(self.db_name in dbs)