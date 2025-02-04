#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # make counter which length is max(a[i]) + 1 = 101 -> O(1)
    max_val = 100
    counter = [0 for i in range(max_val + 1)]

    # count loop a -> O(n) = 100
    for e in a:
        counter[e] += 1

    # return lonely integer when find count 1 -> O(1)
    for i in range(max_val + 1):
        if counter[i] == 1:
            return i


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
