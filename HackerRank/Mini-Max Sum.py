#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    from itertools import combinations

    # Exhaustive Search
    min_sum = int(40e9)
    max_sum = 4

    # O(C(5, 4)) -> 5
    for c in combinations(arr, 4):
        s = sum(c)
        if s < min_sum:
            min_sum = s
        if s > max_sum:
            max_sum = s

    print(min_sum, max_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
