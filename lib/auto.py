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


def ctp(template: str, click_times=1, drag=False):
    """
    click target position

    :param drag:
    :param template: res file path
    :param click_times: zero->target does not have to appear

    """
    # The number of times is used as the criterion for judging whether the click target will appear,
    # that is, 0 means that it may seem, and non-0 means that it will appear
    screenshot_path = "../static/screenshot.png"
    target_path = "../static/target.png"
    # If more than 10 times, the judgment target will not appear?
    count = 10
    # while count:
    while True:
        count = count - 1
        random_sleep()
        screenshot = pag.screenshot()
        screenshot.save(screenshot_path)
        position = matching_picture(template, screenshot_path)
        # region value about (left, top, width , height)
        target = pag.screenshot(region=(position[0][0], position[0][1],
                                        position[1][0] - position[0][0],
                                        position[1][1] - position[0][1]))
        target.save(target_path)
        if ensure_matching(target, template) is False:
            if click_times == 0 and count < 0:
                return False
            elif count < 0:
                exit(10)
                return False
            else:
                count = count - 2
                continue
        else:
            if click_times == 0:
                click_times = click_times + 1
        # click_times must be greater than 0,I'm sure!!!

        if drag:
            pag.moveTo(random_coordinates(position))
            mouse_drag()
        else:
            pag.click(random_coordinates(position), clicks=click_times)
            print('click : ' + template)
        # TODO write json file? Complete control process
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


def mouse_drag(mode='page', index=100):
    sleep(2)
    if mode == 'page':
        pag.dragRel(xOffset=index, yOffset=0, duration=0.25)
    elif mode == 'btn':
        pass
    else:
        pass


def full_mode():
    random_sleep(10)
    pag.getActiveWindow()
    pag.press('F11')
    print("press F11")
