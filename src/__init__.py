#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 13:26
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com

import argparse
from src.process import *
from src.work import *

# select working directory
if 'src' in os.path.abspath('.'):
    os.chdir('./..')
    # print(os.path.abspath('.'))
else:
    dir_list = ['Logs', 'config', 'static']
    for index in dir_list:
        if index not in os.listdir():
            log.error("Missing directories " + index)
        else:
            # work directory true
            # print(os.path.abspath('.'))
            pass

log = dlog(__name__)


def initialize():
    """
    load configuration from conf/conf.toml
    """
    log.debug("initialize...")
    ret = subprocess.run("ping baidu.com -n 1",
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    if ret.returncode:
        log.error('network return code <' + str(ret.returncode) + '> connect failed.')
    else:
        log.info('connect network success.')

    default_conf: dict = Config().load_config()
    if default_conf:
        # TODO Verify the configuration file
        log.info("load default config file success.")
        simulator_path = default_conf['simulator']['path']
        process_config: dict = default_conf["switch"]
        return process_config, simulator_path
    else:
        log.error("Failed to load the default configuration file.")


def control():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uc", help="update config", action="store_true")
    parser.add_argument("--us", help="update source", action="store_true")
    parser.parse_args()
    if parser:
        # print(str(parser))
        pass
