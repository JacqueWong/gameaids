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


# def init_data(func):
#     # @init_data
#     def wrapper(self, *args, **kwargs):
#         if not hasattr(self, 'tgt'):
#             self.tgt = []
#         if not hasattr(self, 'evt'):
#             self.evt = []
#         if not hasattr(self, 'para'):
#             self.para = []
#         # if not hasattr(self, 'list4'):
#         #     self.list4 = []
#         return func(self, *args, **kwargs)
#
#     return wrapper


class Process:
    def __init__(self):
        self.res = Resource()
        self.auto = Auto()
        self.proc = []
        self.tgt = []
        self.evt = []
        self.para = []

    def data_handle(self, tgt: list, evt=None, para=None):
        length = len(tgt)
        if para is None:
            para = [1] * length
        if evt is None:
            evt = [1] * length
        self.tgt.extend(tgt)
        self.evt.extend(evt)
        self.para.extend(para)

    def append_action(self):
        action = [self.tgt.copy(), self.evt.copy(), self.evt.copy()]
        if type(action[0]) is list:
            self.proc.extend(list(map(self.auto.build_action, *action)))
        else:
            self.proc.extend(list(map(self.auto.build_action, action)))

    def action_handle(self, res_list: list, loop_count: int = 1):
        return list(map(self.res.get, res_list * loop_count))

    def do_process(self):
        print("function do process")
        for index in self.proc:
            print(index)
            self.auto.action = index
            # self.auto.do_action()

    # def open_game(self):
    #     print("function open game")
    #     # full_mode()
    #     self.append_action(self.action_handle(['game_icon', 'update_OK', 'start_page']))
    #
    # def gains_crucible(self):
    #     self.append_action(self.action_handle(['crucible', 'ok']))
    #
    # def gains_hourglass(self):
    #     self.append_action(self.action_handle(['ok']))

    # def gains_arena(self):
    #     temp = ['collapse_drop_down_box', 'arena_button']
    #     count = 3
    #     while count:
    #         count = count - 1
    #         temp.extend(['reduce_times', 'ok'])
    #     temp.extend(['daily_rewards', 'leave_4'])
    #     temp_list = [1] * len(temp)
    #     list(map(mtp, list(map(self.res.get, temp)), temp_list))
    #
    # def venture(self):
    #     mtp(self.res.get('expedition_button'), action=-1)
    #     md(mode='page_left')
    #     # self.receive_proceeds()
    #     self.disassemble_equipment()
    #     self.start_venture()
    #
    # def start_venture(self):
    #     suit = ['suit_one', 'suit_two', 'suit_three']
    #     team = ['team_one', 'team_two', 'team_three']
    #     count = 0
    #     while count < 2:
    #         temp = []
    #         temp.extend(['tavern_button', 'suit', suit[count], 'close',
    #                      'leave_3', 'expedition_button', team[count],
    #                      'venture_button', 'sign_deed'])
    #         temp_list = [1] * len(temp)
    #         list(map(mtp, list(map(self.res.get, temp)), temp_list))
    #         mtp(self.res.get('duration_button'), action=-1)
    #         md(mode='btn')
    #         temp = []
    #         temp.extend(['start_task', 'leave_2', 'leave_3'])
    #         temp_list = [1] * len(temp)
    #         list(map(mtp, list(map(self.res.get, temp)), temp_list))
    #         count = count + 1
    #
    # def receive_proceeds(self):
    #     temp = ['expedition_button', 'venture_finish']
    #     count = 3
    #     while count:
    #         count = count - 1
    #         temp.extend(['receive', 'receive_and_leave'])
    #     temp.append('leave_3')
    #     temp_list = [1] * len(temp)
    #     _ = map(mtp, list(map(self.res.get, temp)), temp_list)
    #
    # def disassemble_equipment(self):
    #     temp = ['warehouse_button', 'equip', 'batch_decomposition', 'decompose_purple_gear', 'ok', 'leave_2']
    #     temp_list = [1] * len(temp)
    #     _ = map(mtp, list(map(self.res.get, temp)), temp_list)
    #
    def manor_double_benefit(self):
        print("function mdb.")
        # target = self.action_handle(['expedition_button', 'expedition_button', 'manor_button'])
        # event = [2, 2, 1]
        # para = [101, 101, 1]
        # t = self.action_handle(['double_benefits', 'ok'], 5)
        # target.extend(t)
        # event.extend([1] * (len(t)))
        # para.extend([1] * (len(t)))
        # target.extend(self.action_handle(['leave_3', 'manor_button', 'manor_button']))
        # event.extend([1, 2, 2])
        # para.extend([1, 100, 100])
        # self.append_action([target, event, para])

        self.data_handle(
            tgt=self.action_handle(['expedition_button', 'expedition_button', 'manor_button']),
            evt=[2, 2, 1],
            para=[101, 101, 1]
        )
        self.data_handle(tgt=self.action_handle(['double_benefits', 'ok'], 5))
        self.data_handle(
            tgt=self.action_handle(['leave_3', 'manor_button', 'manor_button']),
            evt=[1, 2, 2],
            para=[1, 100, 100]
        )
        self.append_action()

    #
    # def church_personal_tasks(self):
    #     temp = ['church_button', 'parthenon', 'personal_tasks']
    #     count = 3
    #     while count:
    #         count = count - 1
    #         temp.append('ads_icon')
    #     temp.append('leave_4')
    #     temp_list = [1] * len(temp)
    #     _ = map(mtp, list(map(self.res.get, temp)), temp_list)
    #
    # def market_automatic_purchases(self):
    #     # TODO use ocr will be better?
    #     pass
    #
    # def submissions(self):
    #     pass
    #
    # def login(self):
    #     pass
