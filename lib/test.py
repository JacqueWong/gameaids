#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/12/25 10:06
# @Author  : Jacque
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :
import multiprocessing
import time

from lib import Auto

auto = Auto()
start_time = time.perf_counter()  # 记录开始时间
print(auto.mtp("./../static/target.png", waiting=0))
end_time = time.perf_counter()  # 记录结束时间

elapsed_time = end_time - start_time  # 计算函数执行时间

print(f"函数执行时间: {elapsed_time:0.6f} 秒")  #
