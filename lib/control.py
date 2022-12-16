#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 18:36
# @Author  : Jacque
# @Site    : 
# @File    : control.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :

import os


class ControlApp:
    def __init__(self, app_path: str = None):
        if app_path is None:
            self.app_path = r'C:\Program Files\BlueStacks_nxt_cn\HD-Player.exe'
        else:
            self.app_path = app_path
        self.pr_name = 'HD-Player.exe'

    # start simulator
    def open_app(self):
        os.startfile(self.app_path)

    def close_app(self):
        os.system('%s%s' % ("taskkill /F /IM ", self.pr_name))
