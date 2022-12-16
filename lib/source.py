#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/30 10:20
# @Author  : Jacque
# @Site    : 
# @File    : source.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :
import json
import os


def files_list_to_json(root, files: list):
    json_dict = {}
    for index in files:
        name, _ = os.path.splitext(index)
        temp_dict = {name: os.path.join(root, index)}
        json_dict.update(temp_dict)
    return json_dict


class Source:
    def __init__(self):
        self.base_dict = {
            "name": "Image_path",
            "flag": True,
            "root": "static/",
            "screenshot": "screenshot.png",
        }
        self.source_root = '..\\static'
        self.source_path = '..\\config\\source.json'
        self.source_dict = json.load(fp=open(self.source_path, mode='r'))
        self.source_list = []
        self.__fill_source_list()

    def update_source(self, folder_path: str = None):
        if folder_path is None:
            folder_path = self.source_root
        if not os.path.isdir(folder_path):
            print("folder<" + folder_path + "> does not exist")
            exit(1)
        image_path = {}
        temp_dict = {}
        flag = None
        for root, dirs, files in os.walk(folder_path):
            if dirs:
                if root == folder_path:
                    image_path = dict.fromkeys(dirs)
                else:
                    temp_dict = dict.fromkeys(dirs)
                    if temp_dict:
                        flag = root.split(os.sep)[2]
            if temp_dict:
                for key in temp_dict.keys():
                    if key in root:
                        temp_dict[key] = files_list_to_json(root, files)
                image_path[flag] = temp_dict
            for key in image_path.keys():
                if key in root and image_path[key] is None:
                    image_path[key] = files_list_to_json(root, files)
        res_dict = self.base_dict
        res_dict.update(image_path)
        json.dump(res_dict, fp=open(self.source_path, mode='w'), indent=4)

    def get_all_source(self):
        return self.source_dict

    def get_source(self, name: str = None):
        if not name:
            return False
        if name not in self.source_list:
            return False
        return self.__find_source(self.source_dict, name)

    def __find_source(self, temp_dict, name):
        target_key = None
        for key, value in dict.items(temp_dict):
            if key == name:
                return value
            if type(value) is dict and list.index(self.source_list, key) < list.index(self.source_list, name):
                target_key = key
        return self.__find_source(temp_dict[target_key], name)

    def __fill_source_list(self):
        return self.__record_source(self.source_dict)

    def __record_source(self, temp_dict):
        for key, value in dict.items(temp_dict):
            self.source_list.append(key)
            if type(value) is dict:
                self.__record_source(value)

