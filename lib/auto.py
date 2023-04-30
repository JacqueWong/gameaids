#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 18:29
# @Author  : Jacque
# @Mail    : Jacquewong1111@outlook.com
import sys
import time
import cv2 as cv
import numpy as np
import pyautogui as pag

from lib.log import dlog
from lib.evade import *

log = dlog(__name__)


class Auto:
    def __init__(self):
        self.TIMEOUT_MS = 10000
        self.position = []
        self.non_essential = []
        self.threshold = 0.9
        self.count = 10
        self.action = {
            "step": 0,
            "res": "",
            "event": "",
            "para": 1,
            # "wt": 2,
            # "evade": 10,
            # "remark": ""
        }

    def build_action(self, res, event, para):
        self.action["step"] += 1
        self.action["res"] = res
        self.action["event"] = event
        self.action["para"] = para
        log.debug("build action. action : " + str(self.action.copy()))
        return self.action.copy()

    def do_action(self):
        log.debug("function <do_action> : step :" + str(self.action["step"]))
        try:
            if self.mtp(self.action["res"]):
                # match target ture
                if self.action["event"] == 1:
                    # click
                    pag.click(random_coordinates(self.position), clicks=self.action["para"])
                    log.info("click : " + self.action["res"])
                elif self.action["event"] == 2:
                    # drag
                    pag.moveTo(random_coordinates(self.position))
                    md(mode=self.action["para"])
                elif self.action["event"] == 3:
                    # mouse move
                    pag.moveTo(random_coordinates(self.position))
                else:
                    # return True
                    log.debug("event <" + self.action["event"] + "> not found.")
                    pass
            else:
                if self.action["event"] == 0 and self.action["para"] == 0:
                    log.info("event and para is 0.")
                    return True
                elif self.action["res"].split('\\')[-1].split('.')[0] in self.non_essential:
                    log.debug("Target " + self.action["res"] + " in non-essential list misses.")
                else:
                    pass
                log.error("do action step<" + str(self.action["step"]) + "> failed.")
                return False
        except ValueError:
            log.error("Invalid input <" + self.action["res"] + ">. Please enter a valid file path.")
        except TypeError:
            log.error("Invalid argument type. Please enter the correct type.")
        except Exception as e:
            log.critical("An error occurred:", e)
        else:
            return True
        finally:
            pass
    # Clean up any resources

    def mtp(self, template_path: str, waiting: float = 1.8, reg: list = None):
        """
        match target position

        :param template_path: resource file path
        :param waiting: sleep time
        :param reg: pyautogui region
        """
        count = self.count
        # start_time = time.time()
        template_cv = cv.imdecode(np.fromfile(template_path, dtype=np.uint8), 1)
        th, tw = template_cv.shape[:2]
        log.debug("match <" + template_path + ">.")
        while count:
            count -= 1
            sleep(waiting)
            # Convert screenshot to OpenCV format
            screenshot_cv = cv.cvtColor(np.array(pag.screenshot(region=reg)), cv.COLOR_RGB2BGR)
            result = cv.matchTemplate(screenshot_cv, template_cv, cv.TM_CCORR_NORMED)
            # min_val, max_val, min_loc, max_loc
            _, max_val, _, max_loc = cv.minMaxLoc(result)
            log.debug(str(count) + " max_val : " + str(max_val))

            if self.threshold < max_val:
                self.position = [max_loc, (max_loc[0] + tw, max_loc[1] + th)]
                log.debug("match ture. target<" + template_path + ">, position : " + str(self.position))
                return True

            # current_time = time.time()
            # if current_time - start_time > self.TIMEOUT_MS / 1000:
            #     log.debug("Timeout exits the loop in mtp function.{TIMEOUT_MS}".format(TIMEOUT_MS=self.TIMEOUT_MS))
            #     break
        return False


def md(mode: int = None, index: list = None):
    """
    mouse drag
    """
    log.debug('run function mouse drag. mode : ' + str(mode))
    if mode == 100:
        # page_left
        pag.dragRel(xOffset=75, yOffset=0, duration=0.25)
    elif mode == 101:
        # page_right
        pag.dragRel(xOffset=-75, yOffset=0, duration=0.25)
    elif mode == 110:
        # button
        pag.dragRel(xOffset=200, yOffset=0, duration=0.25)
    else:
        if not index:
            pag.dragRel(xOffset=index[0], yOffset=index[1], duration=index[2])


def full_mode():
    """
    set ActiveWindow full mode
    """
    random_sleep(10)
    pag.getActiveWindow()
    pag.press('F11')
    random_sleep(10)
    log.debug("press F11")
