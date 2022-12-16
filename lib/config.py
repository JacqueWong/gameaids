#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/20 15:27
# @Author  : Jacque
# @Site    : 
# @File    : config.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :
import configparser
import os


class Config:
    def __init__(self, config_path=None):
        self.config_path = r'../config/game.ini'

        if config_path is None:
            config_path = self.config_path
        if not os.path.isfile(config_path):
            print("config file(" + config_path + ") not exist.")
        config = configparser.ConfigParser()
        config.read(config_path, encoding='utf-8')
        sections_list = list(config.sections())
        self.config_dict = dict.fromkeys(sections_list)
        for sec in sections_list:
            options_list = list(config.options(section=sec))
            temp_dict = dict.fromkeys(options_list)
            for op in options_list:
                temp_dict[op] = config.get(section=sec, option=op)
            self.config_dict[sec] = temp_dict

    def get_all_config(self):
        return self.config_dict

    def get_config(self, section_name, key=None):
        if not key:
            return self.config_dict[section_name]
        else:
            return self.config_dict[section_name][key]
