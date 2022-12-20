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


# TODO All functions need to be tested, and the logic is not yet perfect.
#  It also needs to be optimized, using the [map] function
class Process:
    def __init__(self):
        # base class load src
        self.src = Source()

    def open_game(self):
        # full_mode()
        temp = ['game_icon', 'update_OK', 'start_page', 'collapse_drop_down_box']
        var = map(ctp, map(self.src.get(), temp), [1, 0, 0, 1])
        for i in var:
            print(i)

    def gains_crucible(self):
        print('function gains_crucible')
        ctp(self.src.get('crucible'))

    def gains_hourglass(self):
        print('function gains_hourglass')
        ctp(self.src.get('ok'))

    def gains_arena(self):
        print('function gains_arena')
        ctp(self.src.get('arena_button'))
        count = 3
        while count:
            ctp(self.src.get('reduce_times'))
            ctp(self.src.get('ok'))
            count = count - 1
        ctp(self.src.get('daily_rewards'))

    def venture(self):
        self.disassemble_equipment()
        self.receive_proceeds()
        self.start_venture()

    def start_venture(self):
        ctp(self.src.get('tavern_button'))
        # count = 3
        # while count:
        #     count = count -1

    def receive_proceeds(self):
        ctp(self.src.get('venture_finish'))
        count = 3
        while count:
            count = count - 1
        ctp(self.src.get('receive'))
        ctp(self.src.get('receive_and_leave'))

    def disassemble_equipment(self):
        ctp(self.src.get('warehouse_button'))
        ctp(self.src.get('equip'))
        ctp(self.src.get('Batch decomposition'))
        ctp(self.src.get('decompose_purple_gear'))
        ctp(self.src.get('ok'))
        ctp(self.src.get('leave_4'))

    def manor_double_benefit(self):
        ctp(self.src.get('manor_button'))
        count = 5
        while count:
            count = count - 1
            ctp(self.src.get('double_benefits'))
            ctp(self.src.get('ok'))
        ctp(self.src.get('leave_2'))

    def church_personal_tasks(self):
        ctp(self.src.get('parthenon'))
        ctp(self.src.get('personal_tasks'))
        count = 3
        while count:
            count = count - 1
            ctp(self.src.get('ads_icon'))

    def market_automatic_purchases(self):
        pass
