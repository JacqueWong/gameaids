#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 15:46
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com

import logging
import os
import time

from lib.config import Config


def dlog(name):
    if 'src' in os.path.abspath('.') or 'lib' in os.path.abspath('.'):
        os.chdir('./..')
    level = Config().get_config(["log", "level"])
    log_dir = "Logs"
    date_format = "%Y-%m-%d"
    if level == 10:
        log_format = '%(levelname)s \t:' \
                     '%(asctime)s ' \
                     '<%(filename)s>' \
                     '[%(lineno)d]' \
                     ': %(message)s'
    else:
        log_format = '%(levelname)s : %(asctime)s : %(message)s'

    logger = logging.getLogger(name)
    logger.setLevel(level)
    today = time.strftime(date_format, time.localtime())
    file_name = log_dir + "/dxcb2-" + today + ".log"
    if not os.path.isfile(file_name):
        open(file_name, mode='w', encoding="utf-8")
    formatter = logging.Formatter(log_format)
    handler = logging.FileHandler(file_name)
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
