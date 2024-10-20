from itertools import combinations


def solution(number, k):
    answer = ''
    max_num = -1
    n = len(number)
    # O(C(100만, k) * len(number)) -> 5천억 * 100만..
    for c in combinations(number, k):
        temp_number = list(number)

        for i in range(k):
            temp_number.remove(c[i])
        d = int(''.join(temp_number))
        if d > max_num:
            max_num = d
    answer = str(max_num)

    return answer