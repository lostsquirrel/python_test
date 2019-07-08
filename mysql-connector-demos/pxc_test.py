# coding=utf-8
import unittest

import settings
import utils


class PXCTests(unittest.TestCase):

    def setUp(self) -> None:
        self.db_name = 'percona'
        # base_config['database'] = self.db_name
        config181 = settings.get_mysql_config()
        self.conn181 = utils.create_connection(config181)
        config182 = settings.get_mysql_config()
        config182['host'] = '192.168.10.182'
        config182['database'] = self.db_name
        self.conn182 = utils.create_connection(config182)
        config183 = settings.get_mysql_config()
        config183['host'] = '192.168.10.183'

        self.conn183 = utils.create_connection(config183)

    def tearDown(self) -> None:
        for conn in [self.conn181, self.conn182, self.conn183]:
            conn.close()

    def test_sync(self):
        utils.create_database(self.conn182, self.db_name)
        table_sql = "CREATE TABLE example (node_id INT PRIMARY KEY, node_name VARCHAR(30))"
        utils.create_table(self.conn183, table_sql)
        sql = "INSERT INTO percona.example VALUES (%s, %s);"
        val = (1, 'percona1')
        utils.insert(self.conn181, sql, val)
        print(utils.select(self.conn182, "SELECT * FROM percona.example;", None))
