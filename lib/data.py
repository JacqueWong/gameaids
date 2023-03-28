#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/20 10:37
# @Author  : Jacque
# @Site    : 
# @File    : data.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :


import tomllib


def load_data():
    with open("./../config/data.toml", "rb") as f:
        return tomllib.load(f)


print(load_data()["process"]["open_game"])
