#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/23 18:36
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com


from lib.auto import full_mode

import subprocess


class ControlApp:
    def __init__(self, app_path: str = None):
        if app_path is None:
            self.app_path = r'C:\Program Files\BlueStacks_nxt_cn\HD-Player.exe'
        else:
            self.app_path = app_path
        self.proc = None

    def open_app(self):
        self.proc = subprocess.Popen(self.app_path)
        full_mode()

    def close_app(self):
        if self.proc is not None and self.proc.poll() is None:
            self.proc.terminate()
            self.proc.wait()
        self.proc = None
