#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/12 13:38
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com

from lib import Data
from src import Process


class Work(Process):
    def __init__(self):
        super().__init__()
        self.data = Data().load_process_data()
        '''
        self.table = {
            "res": [],
            "lc": 1,
            "evt": None or [],
            "para": None or []
        }
        '''

    def add_action(self, table: dict):
        self.parse_data(table.copy())

    def open_game(self):
        self.add_action(self.data["open_game"])

    def gains_crucible(self):
        self.add_action(self.data["gains_crucible"])

    def gains_hourglass(self):
        self.add_action(self.data["gains_hourglass"])

    def gains_arena(self):
        temp = self.data["gains_arena"]
        self.add_action(temp["begin"])
        self.add_action(temp["loop"])
        self.add_action(temp["end"])

    def venture(self):
        self.add_action(self.data["venture"])
        self.receive_proceeds()
        self.disassemble_equipment()
        self.start_venture()

    def start_venture(self):
        temp = self.data["start_venture"]
        suit = temp["begin"]["suit"]
        team = temp["begin"]["team"]
        tmp = temp["begin"]["res"].copy()
        count = 0
        while count < 3:
            i = tmp.index("suit_index")
            temp["begin"]["res"][i] = suit[count]
            i = tmp.index("team_index")
            temp["begin"]["res"][i] = team[count]
            self.add_action(temp["begin"])
            self.add_action(temp["drag"])
            self.add_action(temp["end"])
            count = count + 1

    def receive_proceeds(self):
        temp = self.data["receive_proceeds"]
        self.add_action(temp["begin"])
        self.add_action(temp["loop"])
        self.add_action(temp["end"])

    def disassemble_equipment(self):
        self.add_action(self.data["disassemble_equipment"])

    def manor_double_benefit(self):
        temp = self.data["manor_double_benefit"]
        self.add_action(temp["begin"])
        self.add_action(temp["loop"])
        self.add_action(temp["end"])

    def church_personal_tasks(self):
        temp = self.data["church_personal_tasks"]
        self.add_action(temp["begin"])
        self.add_action(temp["loop"])
        self.add_action(temp["end"])

    def market_automatic_purchases(self):
        # TODO use ocr will be better?
        pass

    def login(self):
        pass
