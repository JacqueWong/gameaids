#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 15:55
# @Author  : Jacque
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# from lib import *
from src import *
from lib import *


def load_process(temp: dict):
    temp_list = []
    for key, value in temp.items():
        if value == 'on':
            temp_list.append(key)
    if temp_list:
        log.info("load process : " + str(temp_list))
    else:
        log.debug("There are no processes to load.")
    return temp_list


def initialize():
    default_conf: dict = Config(config_path='../config/config.ini').get_all_config()
    if default_conf:
        log.info("load default config file success.")
        path = default_conf['PATH']
        path = path['bluestacks']
        # Configure validation
        author = 'AUTHOR'
        if log.level != 10:
            if author in default_conf.keys():
                if default_conf[author]['name'] == 'Jacque' \
                        and default_conf[author]['email'] == 'Jacquewong1111@outlook.com':
                    log.info("Validation succeeded.")
            else:
                log.error("Validation failed.File<config.ini>[Author].")
                exit(2)
        process_config: dict = default_conf['CONFIG']
        # time_conf: dict = default_conf['TIME']
        # process_config.update(time_conf)
        return process_config, path
    else:
        log.info("Failed to load the default configuration file.")
        exit(3)


def start_work(conf):
    print(config)
    print(conf)


if __name__ == "__main__":
    log = CustomLog().custom_log(level=logging.DEBUG)
    config, app_path = initialize()
    process_list = load_process(config)

    # ca = ControlApp(app_path)
    # game = Game()
    # log.info("open application.")
    # ca.open_app()
    # log.info("open game.")
    # game.open_game()

    start_work(process_list)

    # ca.close_app()
    # log.debug("close application")
    log.info("test main function finish.")

