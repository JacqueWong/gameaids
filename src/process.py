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

    def parse_data(self, table: dict):
        if "lc" in dict.keys(table):
            table["evt"] = None
            table["para"] = None
        if "lc" in dict.keys(table):
            table["lc"] = 1
        self.data_handle(
            res=table["res"],
            loop_count=table["lc"],
            evt=table["evt"],
            para=table["para"]
        )
        self.append_action()

    def data_handle(self, res: list, loop_count: int, evt, para):
        tgt = list(map(self.res.get, res * loop_count))
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
                self.evt.copy())))

    def do_process(self):
        print("function do process")
        for index in self.proc:
            print(index)
            self.auto.action = index
            # self.auto.do_action()

