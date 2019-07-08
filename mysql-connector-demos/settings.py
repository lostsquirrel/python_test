# coding=utf-8
import configparser
import logging

cp = configparser.ConfigParser()
cp.read('config.ini')

logging.basicConfig(level=logging.DEBUG)


def get_mysql_config():
    return cp['mysql']
