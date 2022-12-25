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


# TODO All functions need to be optimized, using the [map] function
class Process:
    def __init__(self):
        self.res = Resource()

    def test(self):
        mtp(self.res.get('expedition_button'), action=-1)
        md(mode='page_right')

    def open_game(self):
        full_mode()
        temp = ['game_icon', 'update_OK', 'start_page', 'collapse_drop_down_box']
        _ = map(mtp, list(map(self.res.get, temp)), [1, 0, 0, 1])

    def gains_crucible(self):
        mtp(self.res.get('crucible'))

    def gains_hourglass(self):
        mtp(self.res.get('ok'))

    def gains_arena(self):
        temp = ['arena_button']
        count = 3
        while count:
            count = count - 1
            temp.extend(['reduce_times', 'ok'])
        temp.extend(['daily_rewards', 'leave_4'])
        temp_list = [1] * len(temp)
        _ = map(mtp, list(map(self.res.get, temp)), temp_list)

    def venture(self):
        mtp(self.res.get('expedition_button'), action=-1)
        md(mode='page_left')
        self.receive_proceeds()
        self.disassemble_equipment()
        self.start_venture()

    def start_venture(self):
        suit = ['suit_one', 'suit_two', 'suit_three']
        team = ['team_one', 'team_two', 'team_three']
        temp = []
        count = 0
        while count < 2:
            temp.extend(['tavern_button', 'suit', suit[count], 'close',
                         'leave_3', 'expedition_button', team[count],
                         'venture_button', 'sign_deed'])
            temp_list = [1] * len(temp)
            _ = map(mtp, list(map(self.res.get, temp)), temp_list)
            mtp(self.res.get('duration_button'), action=-1)
            md(mode='btn')
            temp = []
            temp.extend(['start_task', 'leave_2', 'leave_3'])
            temp_list = [1] * len(temp)
            _ = map(mtp, list(map(self.res.get, temp)), temp_list)
            count = count + 1

    def receive_proceeds(self):
        temp = ['expedition_button', 'venture_finish']
        count = 3
        while count:
            count = count - 1
            temp.extend(['receive', 'receive_and_leave'])
        temp.append('leave_3')
        temp_list = [1] * len(temp)
        _ = map(mtp, list(map(self.res.get, temp)), temp_list)

    def disassemble_equipment(self):
        temp = ['warehouse_button', 'equip', 'batch_decomposition', 'decompose_purple_gear', 'ok', 'leave_2']
        temp_list = [1] * len(temp)
        _ = map(mtp, list(map(self.res.get, temp)), temp_list)

    def manor_double_benefit(self):
        mtp(self.res.get('expedition_button'), action=-1)
        md(mode='page_right')
        md(mode='page_right')
        mtp(self.res.get('manor_button'))
        count = 5
        while count:
            count = count - 1
            mtp(self.res.get('double_benefits'))
            mtp(self.res.get('ok'))
        mtp(self.res.get('leave_3'))
        mtp(self.res.get('manor_button'), action=-1)
        md(mode='page_left')
        md(mode='page_left')

    def church_personal_tasks(self):
        temp = ['church_button', 'parthenon', 'personal_tasks']
        count = 3
        while count:
            count = count - 1
            temp.append('ads_icon')
        temp.append('leave_4')
        temp_list = [1] * len(temp)
        _ = map(mtp, list(map(self.res.get, temp)), temp_list)

    def market_automatic_purchases(self):
        # TODO use ocr will be better?
        pass

    def submissions(self):
        pass

    def login(self):
        pass


Process().test()
