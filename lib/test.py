#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:06
# @Author  : Jacque
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :
import random
from datetime import datetime

import pyautogui as pag

from lib import random_sleep


def rand():
    return int(random.uniform(440, 515)), int(random.uniform(902, 965))


while True:
    x, y = pag.position()
    if 435 < x < 520 and 900 < y < 970:
        pag.click(*rand())
        random_sleep(0.2)
        print('click : ' + str(datetime.today().time()))
