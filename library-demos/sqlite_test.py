import os
import sqlite3 as lite
import unittest


db_path = os.getenv("DB_PATH", "/data/grafana.db")

class TestSqlite3(unittest.TestCase):

    def test_version(self):
        con = lite.connect(db_path)

        with con:
            cur = con.cursor()
            cur.execute('SELECT SQLITE_VERSION()')

            data = cur.fetchone()

            print("SQLite version: %s" % data)

    
    def test_show_tables(self):
        con = lite.connect(db_path)
        sql = '''
        SELECT 
            name
        FROM 
            sqlite_master
        '''
        with con:
            cur = con.cursor()
            cur.execute(sql)
            for row in cur.fetchall():
                print(row)
            self.assertEquals(1,1)