#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/30 10:20
# @Author  : Jacque
# @Site    : 
# @File    : res.py
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


def record_res(temp_dict, ret):
    for key, value in dict.items(temp_dict):
        ret.append(key)
        if type(value) is dict:
            record_res(value, ret)


def fill_res_list(source_dict):
    ret = []
    record_res(source_dict, ret)
    return ret


class Resource:
    def __init__(self):
        self.base_dict = {
            "name": "Image_path",
            "flag": True,
            "root": "static/",
            "screenshot": "screenshot.png",
        }
        self.res_root = '..\\static'
        self.res_path = '..\\config\\source.json'
        self.res_dict = json.load(fp=open(self.res_path, mode='r'))
        self.res_list = fill_res_list(self.res_dict)

    def update_res(self, folder_path: str = None):
        """
        resource folder -> source.json

        :param folder_path: default is static/

        Raises: default save at config/source.json
        """
        if folder_path is None:
            folder_path = self.res_root
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
        json.dump(res_dict, fp=open(self.res_path, mode='w'), indent=4)

    def get_all_res(self):
        return self.res_dict

    def get(self, name: str = None):
        """
        get source by name from source json
        """
        if not name:
            return False
        if name not in self.res_list:
            return False
        return self.__find_res(self.res_dict, name)

    def __find_res(self, temp_dict, name):
        target_key = None
        for key, value in dict.items(temp_dict):
            if key == name:
                print(value)
                return value
            if type(value) is dict and list.index(self.res_list, key) < list.index(self.res_list, name):
                target_key = key
        return self.__find_res(temp_dict[target_key], name)
