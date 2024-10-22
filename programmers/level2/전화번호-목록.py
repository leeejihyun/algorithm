def binary_search(array, target_i, start, end):
    target = array[target_i]
    while start <= end:
        mid = (start + end) // 2
        if (array[mid][:len(target)] == target) and (mid != target_i):
            return mid
        elif array[mid][:len(target)] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

def solution(phone_book):
    answer = True
    n = len(phone_book)

    # 정렬 -> O(NlogN)
    phone_book.sort()

    # 이진 탐색 -> O(logN)
    for i in range(n):
        if binary_search(phone_book, i, 0, n-1):
            return False

    return answer