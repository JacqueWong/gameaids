#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 20:53
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com
import os
import tomllib


def verify_author(files):
    for file in files:
        with open(file, "rb") as fs:
            data: dict = tomllib.load(fs)
            if data['meta']["author"] != "Jacque":
                print("author verify failed.set as default value, please ^_^")


def verify_key(kv: dict, keys: list):
    for key in keys:
        if key in kv.keys():
            pass
        else:
            print(f"Missing key: {key} in config file config.toml.")


def verify():
    if 'lib' in os.path.abspath('.'):
        os.chdir('./..')

    verify_author(['config/data.toml', 'config/config.toml'])

    with open('config/config.toml', "rb") as f:
        config: dict = tomllib.load(f)
        verify_key(config, ['meta', 'simulator', 'switch', 'function', 'log'])

        if not os.path.isfile(config["simulator"]["path"]):
            print("simulator ptah error.")

        verify_key(config["switch"],
                   ['open_game', 'gains_hourglass', 'gains_crucible', 'gains_arena', 'manor_double_benefit',
                    'church_personal_tasks', 'venture', 'market_purchases'])
