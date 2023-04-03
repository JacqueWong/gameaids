#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 15:55
# @Author  : Jacque
# @Site    : 
# @File    : main.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn

from src import *


def load_process(temp: dict):
    temp_list = []
    for key, value in temp.items():
        if value is True:
            temp_list.append(key)
    if temp_list:
        log.info("load process : " + str(temp_list))
    else:
        log.debug("There are no processes to load.")
    return temp_list


def initialize():
    default_conf: dict = Config().load_config()
    if default_conf:
        log.info("load default config file success.")
        simulator_path = default_conf['simulator']['path']
        process_config: dict = default_conf["switch"]
        return process_config, simulator_path
    else:
        log.info("Failed to load the default configuration file.")
        sys.exit(8)


def start_work(work_dict, update=True):
    if update:
        for key, value in dict.items(work_dict):
            if value is True:
                print('process : ' + key)
                log.info("run process : " + key)
                exec('work.' + key + '()')
                work.init_data()
        work.update_record()
        log.info("update record.")
    log.info("do process.")
    work.do_process()


def update_resource():
    res = Resource()
    res.update_res()


if __name__ == "__main__":
    select_wd()

    level = Config().get_config(["log", "level"])
    log = CustomLog().custom_log(level)

    # control()
    check_network()
    # update_resource()
    conf, app_path = initialize()
    load_process(conf)

    work = Work()
    ca = ControlApp(app_path)
    ca.open_app()
    log.info("open application.")
    log.info("start work")
    start_work(conf)

    ca.close_app()
    log.debug("close application")
    log.info("test main function finish.")
    # log.info("finish.")
