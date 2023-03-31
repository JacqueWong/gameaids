#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 15:27
# @Author  : Jacque
# @Site    : 
# @File    : config.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :
import os
import sys
import tomllib


def verify_keys(keys: list, table: dict):
    for index in keys:
        if index in table.keys():
            pass
        else:
            print("config file verify failed. missing key <" + index + ">.")
            sys.exit(5)


def verify(config):
    keys = ["meta", "path", "switch", "function"]
    verify_keys(keys, config)

    meta = config.get("meta")
    if meta["name"] == "config" and meta["author"] == "Jacque":
        pass
    else:
        print("config.meta verify failed. Please restore the default values")
        sys.exit(5)

    simulator_path = config["simulator"]["path"]
    if not os.path.isfile(simulator_path):
        print("simulator_path (" + simulator_path + ") not exist.")
        sys.exit(4)

    switch_keys = ['open_game', 'gains_hourglass', 'gains_crucible', 'manor_double_benefit',
                   'church_personal_tasks', 'venture', 'gains_arena', 'market_purchases']
    verify_keys(switch_keys, config["switch"])

    funcs = ['OCR', 'record', 'log']
    verify_keys(funcs, config["function"])


class Config:
    def __init__(self):
        self.config_path = 'config/config.toml'
        if not os.path.isfile(self.config_path):
            print("config file(" + self.config_path + ") not exist.")
            sys.exit(4)
        with open(self.config_path, "rb") as f:
            self.config_dict = tomllib.load(f)
        # TODO verify by schema?
        # verify(self.config_dict)

    def load_config(self):
        return self.config_dict

    def get_config(self, key: list):
        tmp = self.config_dict
        for index in key:
            tmp = tmp[index]
        return tmp

    # TODO set config, about {time} table in <config.toml>
