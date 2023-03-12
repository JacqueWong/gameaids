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

from src import Process

p = Process()


class Work:
    def __init__(self):
        self.table = {
            "res": [],
            "lc": 1,
            "evt": None or [],
            "para": None or []
        }

# def open_game(self):
#     print("function open game")
#     # full_mode()
#     self.data_handle(['game_icon', 'update_OK', 'start_page'])
#     self.append_action()
#
#
# def gains_crucible(self):
#     self.data_handle(['crucible', 'ok'])
#     self.append_action()
#
#
# def gains_hourglass(self):
#     self.data_handle(['ok'])
#     self.append_action()
#
#
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
#
# def venture(self):
#     mtp(self.res.get('expedition_button'), action=-1)
#     md(mode='page_left')
#     # self.receive_proceeds()
#     self.disassemble_equipment()
#     self.start_venture()
#
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
#
# def disassemble_equipment(self):
#     temp = ['warehouse_button', 'equip', 'batch_decomposition', 'decompose_purple_gear', 'ok', 'leave_2']
#     temp_list = [1] * len(temp)
#     _ = map(mtp, list(map(self.res.get, temp)), temp_list)


def manor_double_benefit(self):
    print("function mdb.")
    table = {
        "res": ['expedition_button', 'expedition_button', 'manor_button'],
        "evt": [2, 2, 1],
        "para": [101, 101, 1]
    }
    p.parse_data(table)
    table = {
        "res": ['double_benefits', 'ok'],
        "loop_count": 5
    }
    p.parse_data(table)
    table = {
        "res": ['leave_3', 'manor_button', 'manor_button'],
        "evt": [1, 2, 2],
        "para": [1, 100, 100]
    }
    p.parse_data(table)

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
#
# def market_automatic_purchases(self):
#     # TODO use ocr will be better?
#     pass
#
#
# def submissions(self):
#     pass
#
#
# def login(self):
#     pass
