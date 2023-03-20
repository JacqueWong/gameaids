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
from src import Process, full_mode


class Work:
    def __init__(self):
        self.p = Process()
        '''
        self.table = {
            "res": [],
            "lc": 1,
            "evt": None or [],
            "para": None or []
        }
        '''

    def open_game(self):
        full_mode()
        table = {
            "res": ['game_icon', 'update_OK', 'start_page']
        }
        self.p.parse_data(table)

    def gains_crucible(self):
        table = {
            "res": ['crucible', 'ok']
        }
        self.p.parse_data(table)

    def gains_hourglass(self):
        table = {
            "res": ['ok']
        }
        self.p.parse_data(table)

    def gains_arena(self):
        table = {
            "res": ['collapse_drop_down_box', 'arena_button']
        }
        self.p.parse_data(table)
        table = {
            "res": ['reduce_times', 'ok'],
            "lc": 3
        }
        self.p.parse_data(table)
        table = {
            "res": ['daily_rewards', 'leave_4']
        }
        self.p.parse_data(table)

    def venture(self):
        table = {
            "res": ['expedition_button'],
            "evt": [2],
            "para": [100]
        }
        self.p.parse_data(table)
        self.receive_proceeds()
        self.disassemble_equipment()
        self.start_venture()

    def start_venture(self):
        suit = ['suit_one', 'suit_two', 'suit_three']
        team = ['team_one', 'team_two', 'team_three']

        count = 0
        while count < 2:
            table = {
                "res": [
                    'tavern_button',
                    'suit',
                    suit[count],
                    'close',
                    'leave_3',
                    'expedition_button',
                    team[count],
                    'venture_button',
                    'sign_deed']
            }
            self.p.parse_data(table)
            table = {
                "res": ['expedition_button'],
                "evt": [2],
                "para": [110]
            }
            self.p.parse_data(table)
            table = {
                "res": ['start_task', 'leave_2', 'leave_3']
            }
            self.p.parse_data(table)
            count = count + 1

    def receive_proceeds(self):
        table = {
            "res": ['expedition_button', 'venture_finish']
        }
        self.p.parse_data(table)
        table = {
            "res": ['receive', 'receive_and_leave'],
            "lc": 3
        }
        self.p.parse_data(table)
        table = {
            "res": ['leave_3']
        }
        self.p.parse_data(table)

    def disassemble_equipment(self):
        table = {
            "res": [
                'warehouse_button',
                'equip',
                'batch_decomposition',
                'decompose_purple_gear',
                'ok',
                'leave_2'
            ]
        }
        self.p.parse_data(table)

    def manor_double_benefit(self):
        table = {
            "res": ['expedition_button', 'expedition_button', 'manor_button'],
            "evt": [2, 2, 1],
            "para": [101, 101, 1]
        }
        self.p.parse_data(table)
        table = {
            "res": ['double_benefits', 'ok'],
            "lc": 5
        }
        self.p.parse_data(table)
        table = {
            "res": ['leave_3', 'manor_button', 'manor_button'],
            "evt": [1, 2, 2],
            "para": [1, 100, 100]
        }
        self.p.parse_data(table)

    def church_personal_tasks(self):
        table = {
            "res": ['church_button', 'parthenon', 'personal_tasks']
        }
        self.p.parse_data(table)
        table = {
            "res": ['ads_icon'],
            "lc": 3
        }
        self.p.parse_data(table)
        table = {
            "res": ['leave_4']
        }
        self.p.parse_data(table)

    def market_automatic_purchases(self):
        # TODO use ocr will be better?
        pass

    def submissions(self):
        pass

    def login(self):
        pass
