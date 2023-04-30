#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/28 16:24
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com

from lib import *


class Process:
    def __init__(self):
        self.res = Resource()
        self.auto = Auto()
        self.proc = []
        self.tgt = []
        self.evt = []
        self.para = []

    def init_data(self, form: dict):
        self.auto.non_essential = form["non_essential"]
        self.auto.TIMEOUT_MS = form["TIMEOUT_MS"]
        self.auto.threshold = form["threshold"]
        self.auto.count = form["count"]

    def reinitialize_data(self):
        self.tgt.clear()
        self.evt.clear()
        self.para.clear()

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
        self.reinitialize_data()

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
        log.debug("action number in process : " + str(len(self.proc.copy())))

    def do_process(self):
        log.info("function do process")
        for index in last_record():
            log.debug(index)
            self.auto.action = index
            self.auto.do_action()

    def update_record(self):
        record(self.proc.copy())
