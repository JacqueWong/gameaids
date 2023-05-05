#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 15:10
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com

import json


def record(process: list):
    with open("config/process.json", mode='w') as file:
        file.write(json.dumps(process))


def last_record():
    with open("config/process.json", mode='r') as file:
        string = file.read()
    return json.loads(string)
