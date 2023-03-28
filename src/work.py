#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/12 13:38
# @Author  : Jacque
# @Site    : 
# @File    : work.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :

"""
The work class is added to separate the data processing and data sources of the process class,
so as to facilitate the subsequent unified processing of data sources

TODO: add data form file or database
"""
from lib import load_data
from src import Process, full_mode


class Work:
    def __init__(self):
        self.p = Process()
        self.data = load_data()
        '''
        self.table = {
            "res": [],
            "lc": 1,
            "evt": None or [],
            "para": None or []
        }
        '''

    def add_action(self, table: dict):
        self.p.parse_data(table)

    def open_game(self):
        full_mode()
        self.add_action(self.data["process"]["open_game"])

    def gains_crucible(self):
        self.add_action(self.data["process"]["gains_crucible"])

    def gains_hourglass(self):
        self.add_action(self.data["process"]["gains_hourglass"])

    def gains_arena(self):
        temp = self.data["process"]["gains_arena"]
        self.add_action(temp["begin"])
        self.add_action(temp["loop"])
        self.add_action(temp["end"])

    def venture(self):
        self.add_action(self.data["process"]["venture"])
        self.receive_proceeds()
        self.disassemble_equipment()
        self.start_venture()

    def start_venture(self):
        temp = self.data["process"]["start_venture"]
        suit = temp["begin"]["suit"]
        team = temp["begin"]["team"]
        res = temp["begin"]["res"]

        count = 0
        while count < 2:
            t = res.copy()
            i = t.index(res, "suit_index")
            res[i] = suit[count]
            i = t.index(res, "team_index")
            res[i] = team[count]
            self.add_action(t)
            self.add_action(temp["drag"])
            self.add_action(temp["end"])
            count = count + 1

    def receive_proceeds(self):
        temp = self.data["process"]["receive_proceeds"]
        self.add_action(temp["begin"])
        self.add_action(temp["loop"])
        self.add_action(temp["end"])

    def disassemble_equipment(self):
        self.add_action(self.data["process"]["disassemble_equipment"])

    def manor_double_benefit(self):
        temp = self.data["process"]["manor_double_benefit"]
        self.add_action(temp["begin"])
        self.add_action(temp["loop"])
        self.add_action(temp["end"])

    def church_personal_tasks(self):
        temp = self.data["process"]["church_personal_tasks"]
        self.add_action(temp["begin"])
        self.add_action(temp["loop"])
        self.add_action(temp["end"])

    def market_automatic_purchases(self):
        # TODO use ocr will be better?
        pass

    def submissions(self):
        pass

    def login(self):
        pass
