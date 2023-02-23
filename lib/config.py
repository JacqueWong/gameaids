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
    def __init__(self):
        self.config_path = 'config/config.ini'
        if not os.path.isfile(self.config_path):
            print("config file(" + self.config_path + ") not exist.")
        self.config_dict = {}
        self.load_config()

    def get_all_config(self):
        return self.config_dict

    def get_config(self, section_name, key=None):
        if not key:
            return self.config_dict[section_name]
        else:
            return self.config_dict[section_name][key]

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.config_path, encoding='utf-8')
        sections_list = list(config.sections())
        self.config_dict = dict.fromkeys(sections_list)
        for sec in sections_list:
            options_list = list(config.options(section=sec))
            temp_dict = dict.fromkeys(options_list)
            for op in options_list:
                temp_dict[op] = config.get(section=sec, option=op)
            self.config_dict[sec] = temp_dict

    def record_config(self, record_dict: dict):
        cf = configparser.ConfigParser()
        cf.add_section('record')
        for key, value in dict.items(record_dict):
            cf.set('record', key, value)
        cf.write(open(self.config_path, 'w+'))
        pass
