# coding=utf-8
import unittest
import settings
import utils


class DatabaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.db_name = 'mysql_connector_test'
        config = settings.get_mysql_config()
        config['database'] = self.db_name
        self.connection = utils.create_connection(config)

    def tearDown(self) -> None:
        self.connection.close()

    def test_create_table(self):
        table_sql = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
        utils.create_table(self.connection, table_sql)
        tables = utils.show_tables(self.connection)
        self.assertTrue('customers' in tables)

    def test_describe_table(self):
        print(utils.describe_table(self.connection, 'customers'))

    def test_alert_table(self):
        table_sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
        utils.create_table(self.connection, table_sql)

    def test_insert(self):
        sql = "INSERT INTO customers (name, address) VALUES (%(name)s, %(address)s)"
        val = {"name": "John", "address": "Highway 21"}
        rowid = utils.insert(self.connection, sql, val)
        print(rowid)
        self.assertTrue(1 <= rowid)

    def test_select(self):
        sql = "SELECT id, name, address FROM customers"
        val = None
        print(utils.select(self.connection, sql, val))