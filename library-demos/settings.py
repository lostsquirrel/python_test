# -*- coding: utf-8 -*-
import logging
import os
import sys


def get_evn(env_name, default_value):
    if env_name in os.environ:
        val = os.environ[env_name]
    else:
        val = default_value

    return val


logging_level_rank = int(get_evn('LOGGING_LEVEL', 0))
logging.StreamHandler(sys.stdout)

logging.basicConfig(level=[logging.DEBUG, logging.INFO][logging_level_rank],
                    format='%(asctime)s %(threadName)s %(name)-12s:%(lineno)d %(levelname)-8s  %(message)s')
