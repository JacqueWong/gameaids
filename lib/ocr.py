#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/12/22 17:17
# @Author  : Jacque
# @Site    : 
# @File    : ocr.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :

import os

import easyocr


class OCR:
    def __init__(self):
        self.reader = easyocr.Reader(['ch_sim', 'en'],
                                     model_storage_directory=os.path.expanduser('~') + '\\.EasyOCR\\model',
                                     download_enabled=False
                                     )

    def rtt(self):
        """
        read target text -> [../static/target.png]
        """
        target_path = '../static/target.png'
        if os.path.isfile(target_path):
            return self.reader.readtext(target_path)
        else:
            return False

    def rst(self):
        """
        read screenshot text -> [../static/screenshot.png]
        """
        target_path = '../static/screenshot.png'
        if os.path.isfile(target_path):
            return self.reader.readtext(target_path)
        else:
            return False

    def rit(self, img_path: str):
        """
        read image text
        """
        if not os.path.isfile(img_path):
            return False
        return self.reader.readtext(img_path)
