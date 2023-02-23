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


def mtp(template: str, action=1):
    # print("function mtp running...")
    """
    match target position, default click

    :param template: res file path
    :param action: action after successful matching

    Raises:
        action > 1  -> click times                \n
        action = 0  -> if target appears, click   \n
        action = -1 -> target need to drag        \n
    """
    # The number of times is used as the criterion for judging whether the click target will appear,
    # that is, 0 means that it may seem, and non-0 means that it will appear
    screenshot_path = "static/screenshot.png"
    target_path = "static/target.png"
    # If more than 10 times, the judgment target will not appear?
    count = 10
    # while count:
    while True:
        count = count - 1
        random_sleep(2)
        screenshot = pag.screenshot()
        screenshot.save(screenshot_path)
        position = matching_picture(template, screenshot_path)
        # region value about (left, top, width , height)
        target = pag.screenshot(region=(position[0][0], position[0][1],
                                        position[1][0] - position[0][0],
                                        position[1][1] - position[0][1]))
        target.save(target_path)
        if ensure_matching(target, template) is False:
            if action == 0 and count < 0:
                return False
            elif count < 0:
                return False
            else:
                count = count - 2
                continue
        else:
            if action == 0:
                action = action + 1
        if action == -1:
            pag.moveTo(random_coordinates(position))
        else:
            pag.click(random_coordinates(position), clicks=action)
            print('click : ' + template)
        # TODO write json file? record control process
        # action list , about count/index/steps,click/drag button name/icon,times/length,range,mark
        # action = [1, 'click', 'tavern_button', 1, [0, 0, 1, 1], 'Enter the tavern']
        # maybe dict better than list
        # action = {
        #     'step': 1,
        #     'event': 'click',
        #     'target': 'tavern_button',
        #     'parameter': 1,
        #     'evade': 10,
        #     'remarks': 'Enter the tavern'
        # }
        return True


def md(mode: str = None, index: list = None):
    """
    mouse drag
    """
    sleep(2)
    if mode == 'page_left':
        pag.dragRel(xOffset=75, yOffset=0, duration=0.25)
    elif mode == 'page_right':
        pag.dragRel(xOffset=-75, yOffset=0, duration=0.25)
    elif mode == 'btn':
        pag.dragRel(xOffset=200, yOffset=0, duration=0.25)
    else:
        if not index:
            pag.dragRel(xOffset=index[0], yOffset=index[1], duration=index[2])


def full_mode():
    random_sleep(15)
    pag.getActiveWindow()
    pag.press('F11')
    # print("press F11")
