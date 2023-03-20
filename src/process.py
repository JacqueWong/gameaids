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
        if "lc" in dict.keys(table):
            table["evt"] = None
            table["para"] = None
        else:
            table["lc"] = 1
        if "evt" not in dict.keys(table):
            table["evt"] = None
            table["para"] = None
        self.data_handle(
            res=table["res"],
            loop_count=table["lc"],
            evt=table["evt"],
            para=table["para"]
        )
        self.append_action()

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

    def do_process(self):
        print("function do process")
        # update_excel(self.proc)
        for index in self.proc:
            print(index)
        #     self.auto.action = index
        #     # self.auto.do_action()
