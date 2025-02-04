
#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
    # O(n) -> 10^6
    n = len(arr)

    # O(n) -> 10^6
    if len(set(arr)) == 1:
        return arr[0]

    # O(nlogn) -> 10^6 * log2^20 = 20^7
    # sort arr
    arr.sort()

    median = n // 2
    return arr[median]
