#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 15:55
# @Author  : Jacque
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn


from src import *
import subprocess


def check_network():
    ret = subprocess.run("ping baidu.com -n 1",
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    if ret.returncode:
        log.error('network return code <' + str(ret.returncode) + '> connect failed.')
        exit(4)
    else:
        log.info('connect success.')


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


def start_work(work_dict):
    # print(work_dict)
    # Config().record_config(record)
    for key, value in dict.items(work_dict):
        if value == 'on':
            print('proc.' + key + '()')
            exec('proc.' + key + '()')


if __name__ == "__main__":
    log = CustomLog().custom_log(level=logging.DEBUG)
    conf, app_path = initialize()
    check_network()
    load_process(conf)

    proc = Process()
    ca = ControlApp(app_path)
    ca.open_app()
    log.info("open application.")
    proc.open_game()
    log.info("open game.")
    # log.info("start work")
    # start_work(conf)

    # ca.close_app()
    # log.debug("close application")
    log.info("test main function finish.")
