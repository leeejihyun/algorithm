#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Time complexity: O(1)
    # parse PM/AM
    ampm = s[-2:]
    # parse hh, mm, ss
    ps = s.split(':')
    hh, mm, ss = int(ps[0]), ps[1], ps[2][:2]
    # if AM, -12
    if (ampm == 'AM') and (hh == 12):
        hh -= 12
    # elif PM, +12
    elif (ampm == 'PM') and (hh < 12):
        hh += 12
    # make string output
    return '{:02d}:{}:{}'.format(hh, mm, ss)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
