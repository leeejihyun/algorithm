#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # O(n)
    # loop n(=m)
    lsum, rsum = 0, 0
    for i in range(n):
        # left-to-right diagonal sum
        lsum += arr[i][i]
        # right to left diagonal sum
        rsum += arr[i][n - 1 - i]

    # calculate Their absolute difference
    return abs(lsum - rsum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
