#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 16:52
# @Author  : Jacque
# @Site    : 
# @File    : matching.py
# @Software: PyCharm
# @Mail    : Jacquewong@stu.jluzh.edu.cn
# @Desc    :

import cv2 as cv
import numpy as np
from PIL import Image
from PIL.Image import Resampling


def matching_picture(template_path: str, target_path: str):
    """
    Returns the location of the area in the target image that most closely resembles the template
    """

    method = cv.TM_CCOEFF
    target = cv.imdecode(np.fromfile(target_path, dtype=np.uint8), 1)
    template = cv.imdecode(np.fromfile(template_path, dtype=np.uint8), 1)

    th, tw = template.shape[:2]
    result = cv.matchTemplate(target, template, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if method == cv.TM_SQDIFF_NORMED:
        tl = min_loc
    else:
        tl = max_loc
    # br is the coordinate of the point in the lower-right corner of the rectangle
    br = (tl[0] + tw, tl[1] + th)

    return [tl, br]


# The mean hash algorithm is used to calculate the similarity
def calculate_distance(img1, img2):
    str1, str2 = get_hash(img1), get_hash(img2)
    if len(str1) != len(str2):
        return
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count


# noinspection PyMethodMayBeStatic
def get_hash(img):
    if type(img) is str:  # The parameter may be the path of the image
        img = Image.open(img)
    # img.show()
    img = img.resize((16, 16), Resampling.LANCZOS).convert('L')  # Anti aliasing Grayscale
    avg = sum(list(img.getdata())) / 256  # Calculate the pixel average
    s = ''.join(map(lambda i: '0' if i < avg else '1', img.getdata()))  # For each pixel,
    # the value greater than AVG is 1, otherwise it is 0
    return ''.join(map(lambda j: '%x' % int(s[j:j + 4], 2), range(0, 256, 4)))
