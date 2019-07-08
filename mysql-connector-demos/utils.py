# coding=utf-8
from mysql import connector
import logging

logger = logging.getLogger(__name__)


def create_connection(config):
    return connector.connect(**config)


def create_database(connection, database_name):
    cursor = connection.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_general_ci"
    try:
        cursor.execute(sql % database_name)
        logger.debug(cursor.statement)
    except Exception as e:
        logger.error(e)
    finally:
        cursor.close()


def show_databases(connection):
    cursor = connection.cursor()
    sql = "SHOW DATABASES"
    try:
        cursor.execute(sql)
        return list(map(lambda x: x[0], cursor.fetchall()))
    except Exception as e:
        logger.error(e)
    finally:
        cursor.close()


def create_table(connection, table_sql):
    cursor = connection.cursor()
    try:
        cursor.execute(table_sql)
    except Exception as e:
        logger.error(e)
    finally:
        cursor.close()


def show_tables(connection):
    cursor = connection.cursor()
    sql = "SHOW TABLES"
    try:
        cursor.execute(sql)
        return list(map(lambda x: x[0], cursor.fetchall()))
    except Exception as e:
        logger.error(e)
    finally:
        cursor.close()


def describe_table(connection, table_name):
    cursor = connection.cursor(dictionary=True)
    sql = "desc {}".format(table_name)
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        logger.error(e)
    finally:
        cursor.close()


def insert(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        return cursor.lastrowid
    except Exception as e:
        connection.rollback()
        logger.error(e)
    finally:
        cursor.close()


def insert_many(connection, sql, vals):
    cursor = connection.cursor()
    try:
        cursor.execute_many(sql, vals)
        return cursor.rowcount
    except Exception as e:
        logger.error(e)
    finally:
        cursor.close()


def select(connection, sql, param):
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(sql, param)
        return cursor.fetchall()
    except Exception as e:
        logger.error(e)
    finally:
        cursor.close()
