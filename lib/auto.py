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


def __ensure_matching(position, template, confidence=25):
    # region value about (left, top, width , height)
    temp = pag.screenshot(region=(position[0][0], position[0][1],
                                  position[1][0] - position[0][0],
                                  position[1][1] - position[0][1]))
    ret = calculate_distance(template, temp)
    # print('confidence : ' + str(ret))
    if ret > confidence:
        return False
    else:
        return True


def click_target_position(template: str, click_times=1):
    # The number of times is used as the criterion for judging whether the click target will appear,
    # that is, 0 means that it may seem, and non-0 means that it will appear
    target = "../static/screenshot.png"
    # If more than 10 times, the judgment target will not appear?
    count = 10
    # while count:
    while True:
        count = count - 1
        random_sleep()
        screenshot = pag.screenshot()
        screenshot.save(target)
        position = matching_picture(template, target)
        if __ensure_matching(position, template) is False:
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
        pag.click(random_coordinates(position=position), clicks=click_times)
        # print("click: " + template)
        return True


def full_mode():
    random_sleep(8)
    # pag.getActiveWindow()
    pag.press('F11')
    print("press F11")
