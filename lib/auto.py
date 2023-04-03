#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 18:29
# @Author  : Jacque
# @Site    : 
# @File    : auto.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :

import pyautogui as pag
from lib.matching import *
from lib.evade import *


class Auto:
    def __init__(self):
        self.screenshot_path = "static/screenshot.png"
        self.target_path = "static/target.png"
        self.position = []
        self.count = 10
        self.action = {
            "step": 0,
            "res": "",
            "event": "",
            "para": 1,
            # "wt": 2,
            # "evade": 10,
            # "remark": ""
        }

    def build_action(self, res, event, para):
        self.action["step"] += 1
        self.action["res"] = res
        self.action["event"] = event
        self.action["para"] = para
        return self.action.copy()

    def do_action(self):
        # print("function do action")
        # print("resource :" + str(self.action["res"]))
        if self.mtp(self.action["res"]):
            # match target
            if self.action["event"] == 1:
                # click
                # if (self.action["para"] == 0) mouse move only
                pag.click(random_coordinates(self.position), clicks=self.action["para"])
                print("click : " + self.action["res"])
            elif self.action["event"] == 2:
                # drag
                pag.moveTo(random_coordinates(self.position))
                md(mode=self.action["para"])
            elif self.action["event"] == 3:
                # mouse move
                pag.moveTo(random_coordinates(self.position))
            else:
                return True
        else:
            if self.action["event"] == 1 and self.action["para"] == 0:
                return True
            return False

    def mtp(self, template: str, waiting: int = 2):
        """
        match target position

        :param waiting: sleep time
        :param template: res file path
        """
        # print("function mtp running...")
        count = self.count
        while count:
            count -= 1
            sleep(waiting)
            # print("count : " + str(count))
            pag.screenshot().save(self.screenshot_path)
            position = matching_picture(template, self.screenshot_path)
            # region value about (left, top, width , height)
            target = pag.screenshot(
                region=(position[0][0], position[0][1],
                        position[1][0] - position[0][0],
                        position[1][1] - position[0][1]))
            target.save(self.target_path)
            if ensure_matching(target, template):
                # print("match true.")
                self.position = position
                return True
        return False


def md(mode: int = None, index: list = None):
    """
    mouse drag
    """
    if mode == 100:
        # page_left
        pag.dragRel(xOffset=75, yOffset=0, duration=0.25)
    elif mode == 101:
        # page_right
        pag.dragRel(xOffset=-75, yOffset=0, duration=0.25)
    elif mode == 110:
        # button
        pag.dragRel(xOffset=200, yOffset=0, duration=0.25)
    else:
        if not index:
            pag.dragRel(xOffset=index[0], yOffset=index[1], duration=index[2])


def full_mode():
    """
    set ActiveWindow full mode
    """
    random_sleep(10)
    pag.getActiveWindow()
    pag.press('F11')
    # print("press F11")
