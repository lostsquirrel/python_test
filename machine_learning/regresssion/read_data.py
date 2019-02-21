# encoding utf-8

import sqlite3
import pandas as pd

data_path = "/home/lisong/data-science/soccer"
data_file_name = 'database.sqlite'

# Create your connection.
cnx = sqlite3.connect('{}/{}'.format(data_path, data_file_name))
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)


def overview():
    print(df.head())
    print(df.shape)
    print(df.columns)


if __name__ == '__main__':
    overview()
