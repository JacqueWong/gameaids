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
        self.res = Resource()

    def test(self):
        ctp(self.res.get('expedition'), drag=True)

    def main_page_drag(self):
        # TODO Next task
        pass

    def open_game(self):
        full_mode()
        temp = ['game_icon', 'update_OK', 'start_page', 'collapse_drop_down_box']
        var = map(ctp, list(map(self.res.get, temp)), [1, 0, 0, 1])
        print(list(var))

    def gains_crucible(self):
        # print('function gains_crucible')
        ctp(self.res.get('crucible'))

    def gains_hourglass(self):
        print('function gains_hourglass')
        ctp(self.res.get('ok'))

    def gains_arena(self):
        print('function gains_arena')
        ctp(self.res.get('arena_button'))
        count = 3
        while count:
            ctp(self.res.get('reduce_times'))
            ctp(self.res.get('ok'))
            count = count - 1
        ctp(self.res.get('daily_rewards'))
        ctp(self.res.get('leave_4'))

    def venture(self):
        self.receive_proceeds()
        # TODO page need Move horizontally
        self.disassemble_equipment()
        # TODO page need Move horizontally
        self.start_venture()

    def start_venture(self):
        suit = ['suit_one', 'suit_two', 'suit_three']
        team = ['team_one', 'team_two', 'team_three']
        count = 0
        while count < 2:
            ctp(self.res.get('tavern_button'))
            ctp(self.res.get('suit'))
            ctp(self.res.get(suit[count]))
            # ctp(self.res.get('ok'), 0)
            ctp(self.res.get('close'))
            ctp(self.res.get('leave_3'))
            ctp(self.res.get('expedition_button'))
            ctp(self.res.get(team[count]))
            ctp(self.res.get('venture_button'))
            ctp(self.res.get('sign_deed'))
            # TODO btn need Move horizontally
            ctp(self.res.get('duration_button'))
            ctp(self.res.get('start_task'))
            ctp(self.res.get('leave_2'))
            ctp(self.res.get('leave_3'))
            count = count + 1

    def receive_proceeds(self):
        ctp(self.res.get('expedition_button'))
        ctp(self.res.get('venture_finish'))
        count = 3
        while count:
            count = count - 1
            ctp(self.res.get('receive'))
            ctp(self.res.get('receive_and_leave'))
        # TODO leave btn need

    def disassemble_equipment(self):
        ctp(self.res.get('warehouse_button'))
        ctp(self.res.get('equip'))
        ctp(self.res.get('Batch decomposition'))
        ctp(self.res.get('decompose_purple_gear'))
        ctp(self.res.get('ok'))
        ctp(self.res.get('leave_2'))

    def manor_double_benefit(self):
        ctp(self.res.get('manor_button'))
        count = 5
        while count:
            count = count - 1
            ctp(self.res.get('double_benefits'))
            ctp(self.res.get('ok'))
        ctp(self.res.get('leave_3'))

    def church_personal_tasks(self):
        ctp(self.res.get('church_button'))
        ctp(self.res.get('parthenon'))
        ctp(self.res.get('personal_tasks'))
        count = 3
        while count:
            count = count - 1
            ctp(self.res.get('ads_icon'))
        ctp(self.res.get('leave_4'))

    def market_automatic_purchases(self):
        # TODO use ocr will better
        pass


Process().test()
