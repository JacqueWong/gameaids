#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 13:26
# @Author  : Jacque
# @Site    : 
# @File    : __init__.py.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
import argparse
import subprocess

from src.process import *
from src.work import *


def select_wd():
    # select working directory
    if 'src' in os.path.abspath('.'):
        os.chdir('./..')
        # print(os.path.abspath('.'))
    else:
        dir_list = ['Logs', 'config', 'static', 'model']
        for index in dir_list:
            if index not in os.listdir():
                print("Missing directories " + index)
                sys.exit(6)
            else:
                # work directory true
                pass


def check_network():
    ret = subprocess.run("ping baidu.com -n 1",
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    if ret.returncode:
        print('network return code <' + str(ret.returncode) + '> connect failed.')
        sys.exit(7)
    # else:
    #     log.info('connect network success.')


def control():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uc", help="update config", action="store_true")
    parser.add_argument("--us", help="update source", action="store_true")
    parser.parse_args()
    if parser:
        # print(str(parser))
        pass



