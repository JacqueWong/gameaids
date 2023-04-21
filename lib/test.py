#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:06
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com


import time

from lib import Auto

auto = Auto()
start_time = time.perf_counter()
print(auto.mtp("./../static/target.png", waiting=0))
end_time = time.perf_counter()

elapsed_time = end_time - start_time

print(f"函数执行时间: {elapsed_time:0.6f} s")  #
