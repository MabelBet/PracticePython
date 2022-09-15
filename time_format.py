#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    s = input().strip()

    is_pm = s[-2:].lower() == 'pm'
    time_list = list(map(int, s[:-2].split(':')))

    if is_pm and time_list[0] < 12:
        time_list[0] += 12

    if not is_pm and time_list[0] == 12:
        time_list[0] = 0

    return print(':'.join(map(lambda x: str(x).rjust(2, '0'), time_list)))
timeConversion("11:23pm")
    