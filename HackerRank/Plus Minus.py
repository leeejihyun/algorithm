#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    p_cnt, n_cnt, z_cnt = 0, 0, 0

    # Time complexity: O(n) -> 100
    for a in arr:
        # positive count
        if a > 0:
            p_cnt += 1
        # negative count
        elif a < 0:
            n_cnt += 1
        # zero count
        else:
            z_cnt += 1

    # print proportions
    n = len(arr)
    print("{:.6f}".format(p_cnt / n))
    print("{:.6f}".format(n_cnt / n))
    print("{:.6f}".format(z_cnt / n))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
