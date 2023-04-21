#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/20 10:37
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com

import tomllib


class Data:
    def __init__(self):
        with open("config/data.toml", "rb") as f:
            self.data = tomllib.load(f)

    def load_data(self):
        return self.data

    def load_process_data(self):
        return self.data["process"]
