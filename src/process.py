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
        # base class load source
        self.source = Source()
        self.process = []


# TODO many many many many many logical modules(all the 'pass') need to be done
class Game(Process):
    def open_game(self):
        full_mode()
        temp = [
            [self.source.get_source('game_icon'), 1],
            [self.source.get_source('update_OK'), 0],
            [self.source.get_source('start_page'), 0],
            [self.source.get_source('collapse_drop_down_box'), 1]
        ]
        for i, j in temp:
            print(i, j)


class Gains(Process):
    def gains(self):
        pass

    def gains_crucible(self):
        pass

    def gains_hourglass(self):
        pass

    def gains_arena(self):
        pass


class Venture(Process):
    def __init__(self):
        super().__init__()
        # TODO write json file? Complete control process
        # action list , about count/index/steps,click/drag button name/icon,times/length,range,mark
        # self.action = [1, 'click', 'tavern_button', 1, [0, 0, 1, 1], 'Enter the tavern']
        # maybe dict better than list
        # self.action = {
        #     'step': 1,
        #     'event': 'click',
        #     'target': 'tavern_button',
        #     'parameter': 1,
        #     'evade': 10,
        #     'remarks': 'Enter the tavern'
        # }
        # self.action = {
        #     'step': 666,
        #     'event': 'drag',
        #     'target': 'duration_button',
        #     'parameter': 400,
        #     'evade': 10,
        #     'remarks': 'Set adventure time, 8 hours'
        # }

    def start_venture(self):
        pass

    def receive_proceeds(self):
        pass

    def disassemble_equipment(self):
        pass


class Benefit(Process):
    def times(self):
        pass

    def manor_double_benefit(self):
        pass


class Church(Process):
    def last_time(self):
        pass

    def church_personal_tasks(self):
        pass


class Market(Process):
    def last_time(self):
        pass

    def next_time(self):
        pass

    def market_automatic_purchases(self):
        pass
