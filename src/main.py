#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 15:55
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com

from src import *


def start_work(work_dict, update=True):
    if update:
        for key, value in dict.items(work_dict):
            if value is True:
                log.info("add process : " + key)
                exec('work.' + key + '()')
                work.reinitialize_data()
        work.update_record()
        log.info("update record.")
    log.info("do process.")
    work.do_process()


if __name__ == "__main__":
    # control()
    conf, app_path = initialize()

    work = Work()
    ca = ControlApp(app_path)
    ca.open_app()
    log.info("open application.")
    log.info("start work")
    start_work(conf)

    ca.close_app()
    log.info("close application")
    log.info("finish.")
