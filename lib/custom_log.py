#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 15:46
# @Author  : Jacque
# @Site    : 
# @File    : custom_log.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn

import logging
import os
import time


class CustomLog:
    def __init__(self):
        self.__log_dir = "Logs"
        self.__file_name = ''
        self.__date_format = "%Y-%m-%d"
        self.__log_format = '[%(asctime)s]' \
                            '[%(levelname)s]' \
                            '[%(filename)s]' \
                            '[%(lineno)d] ' \
                            '\t%(message)s'

    # Determine whether the log file already exists, and if not, create a new file
    def __determine_log_file_exists(self):
        if not os.path.isfile(self.__file_name):
            open(self.__file_name, mode='w', encoding="utf-8")

    # Log files are stored on a daily basis
    def __custom_log_file_name(self):
        today = time.strftime(self.__date_format, time.localtime())
        self.__file_name = self.__log_dir + "/dxcb2-" + today + ".log"

    def custom_log(self, level=logging.INFO):
        logger = logging.getLogger(__name__)
        logger.setLevel(level=level)
        formatter = logging.Formatter(self.__log_format)
        self.__custom_log_file_name()
        self.__determine_log_file_exists()
        handler = logging.FileHandler(self.__file_name)
        handler.setLevel(level=level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger
