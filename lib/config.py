#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 15:27
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com


import tomllib


class Config:
    def __init__(self):
        self.config_path = 'config/config.toml'
        with open(self.config_path, "rb") as f:
            self.config_dict = tomllib.load(f)

    def load_config(self):
        return self.config_dict

    def get_config(self, key: list):
        tmp = self.config_dict
        for index in key:
            tmp = tmp[index]
        return tmp

    # TODO set config, about {time} table in <config.toml>
