# coding=utf-8
import unittest
import pymssql

server = 'rm-m5e607zl7t092bd1tyo.sqlserver.rds.aliyuncs.com'
user = 'midqdsd'
password = 'midqdsdpwd1_'
database = 'MidDB_QDSD'
port = "3433"


class MSSQLTest(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = pymssql.connect(server=server, user=user,
                                    password=password, database=database, port=port)

    def tearDown(self) -> None:
        self.conn.close()

    def test_create_table(self):
        cursor = self.conn.cursor()
        sql = '''
            CREATE TABLE test (
                id INT PRIMARY KEY IDENTITY (1, 1),
                msg VARCHAR(20)
            );
        '''
        cursor.execute(sql)
        self.conn.commit()

    def test_insert(self):
        cursor = self.conn.cursor()
        for x in range(20):
            cursor.execute("INSERT test (msg)  VALUES ('xxx {}')".format(x))

        self.conn.commit()

    def test_select(self):
        cursor = self.conn.cursor()
        cursor.execute("select * from test")
        row = cursor.fetchone()
        while row:
            print("{} {}".format(*row))
            row = cursor.fetchone()