#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/28 16:24
# @Author  : Jacque
# @Site    : 
# @File    : process.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :

from lib import *


class Process:
    def __init__(self):
        self.res = Resource()
        self.auto = Auto()
        self.proc = []
        self.tgt = []
        self.evt = []
        self.para = []

    def init_data(self):
        self.tgt = []
        self.evt = []
        self.para = []

    def parse_data(self, table: dict):
        if "loop_count" in dict.keys(table):
            table["event"] = None
            table["parameter"] = None
        else:
            table["loop_count"] = 1
        if "event" not in dict.keys(table):
            table["event"] = None
            table["parameter"] = None
        self.data_handle(
            res=table["res"],
            loop_count=table["loop_count"],
            evt=table["event"],
            para=table["parameter"]
        )
        self.append_action()
        self.init_data()

    def data_handle(self, res: list, loop_count: int, evt, para):
        tgt = list(map(self.res.get, res * loop_count))
        # while False in tgt:
        #     tgt.remove(False)
        length = len(tgt)
        if para is None:
            para = [1] * length
        if evt is None:
            evt = [1] * length
        self.tgt.extend(tgt)
        self.evt.extend(evt)
        self.para.extend(para)

    def append_action(self):
        self.proc.extend(list(
            map(
                self.auto.build_action,
                self.tgt.copy(),
                self.evt.copy(),
                self.para.copy())))
        # print(len(self.proc.copy()))

    def do_process(self):
        print("function do process")
        for index in last_record():
            # print(index)
            self.auto.action = index
            self.auto.do_action()

    def update_record(self):
        record(self.proc.copy())
