#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/19 18:19
# @Author  : Jacque
# @Site    : 
# @File    : evade.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :


import random
from time import sleep


def random_coordinates(position: list):
    """
    Returns random coordinates within a range

    :return: coordination_x, coordination_y
    """
    # evade_value
    ev = 1
    if position[1][1] - position[0][1] > 100 and \
            position[1][0] - position[0][0] > 100:
        ev = 25
    coordination_x = random.uniform(position[0][0] + ev, position[1][0] - ev)
    coordination_y = random.uniform(position[0][1] + ev, position[1][1] - ev)
    return int(coordination_x), int(coordination_y)


def random_sleep(base=1, multiple=2):
    sleep(base + random.random() * multiple)

