#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/20 10:37
# @Author  : Jacque
# @Site    : 
# @File    : data.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :
import sys
import tomllib


def verify(data: dict):
    meta = data["meta"]
    if meta["name"] == "data" \
            and type(meta["version"]) is float or int or str \
            and meta["author"] == "Jacque":
        pass
    # TODO add process key verify, maybe key from source file?
    else:
        print("verify data file <data.toml> failed.")
        sys.exit(202)


class Data:
    def __init__(self):
        with open("config/data.toml", "rb") as f:
            self.data = tomllib.load(f)
            verify(self.data)

    def load_data(self):
        return self.data

    def load_process_data(self):
        return self.data["process"]
