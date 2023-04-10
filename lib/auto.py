#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 18:29
# @Author  : Jacque
# @Site    : 
# @File    : auto.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :
import time
import cv2 as cv
import numpy as np
import pyautogui as pag
from lib.evade import *


class Auto:
    def __init__(self):
        self.TIMEOUT_MS = 10000
        self.position = []
        self.threshold = 0.9
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
            if self.action["event"] == 0 and self.action["para"] == 0:
                return True
            return False

    def mtp(self, template_path: str, waiting: float = 0.8, reg: list = None):
        """
        match target position

        :param template_path: resource file path
        :param waiting: sleep time
        :param reg: pyautogui region
        """
        count = self.count
        start_time = time.time()
        template_cv = cv.imdecode(np.fromfile(template_path, dtype=np.uint8), 1)
        while count:
            count -= 1
            sleep(waiting)
            # Convert screenshot to OpenCV format
            screenshot_cv = cv.cvtColor(np.array(pag.screenshot(region=reg)), cv.COLOR_RGB2BGR)
            th, tw = template_cv.shape[:2]

            result = cv.matchTemplate(screenshot_cv, template_cv, cv.TM_CCOEFF_NORMED)
            # min_val, max_val, min_loc, max_loc
            _, max_val, _, max_loc = cv.minMaxLoc(result)
            # print(max_val)

            if self.threshold < max_val:
                self.position = [max_loc, (max_loc[0] + tw, max_loc[1] + th)]
                # print(self.position)
                return True

            current_time = time.time()
            if current_time - start_time > self.TIMEOUT_MS / 1000:
                break
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
