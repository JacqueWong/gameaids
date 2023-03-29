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
import argparse


def check_network():
    ret = subprocess.run("ping baidu.com -n 1",
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    if ret.returncode:
        log.error('network return code <' + str(ret.returncode) + '> connect failed.')
        sys.exit(4)
    else:
        log.info('connect network success.')


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
        path = default_conf['path']
        simulator_path = path['simulator']
        process_config: dict = default_conf["switch"]
        return process_config, simulator_path
    else:
        log.info("Failed to load the default configuration file.")
        sys.exit(3)


def start_work(work_dict):
    for key, value in dict.items(work_dict):
        if value is True:
            print('process : ' + key)
            exec('work.' + key + '()')
            work.p.init_data()
    work.p.do_process()


def control():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uc", help="update config", action="store_true")
    parser.add_argument("--us", help="update source", action="store_true")
    parser.parse_args()
    if parser:
        # print(str(parser))
        pass


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
                sys.exit(9)
            else:
                # work directory true
                pass


def update_resource():
    res = Resource()
    res.update_res()


if __name__ == "__main__":
    # control()
    select_wd()
    # update_resource()
    log = CustomLog().custom_log(level=logging.DEBUG)
    conf, app_path = initialize()
    check_network()
    load_process(conf)

    # proc = Process()
    work = Work()
    # ca = ControlApp(app_path)
    # ca.open_app()
    # log.info("open application.")
    # log.info("start work")
    start_work(conf)
    # proc.do_process()

    # ca.close_app()
    # log.debug("close application")
    log.info("test main function finish.")
    # log.info("finish.")
