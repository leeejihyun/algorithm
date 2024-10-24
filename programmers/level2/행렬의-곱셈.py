def solution(arr1, arr2):
    n, m = len(arr1), len(arr1[0])
    m, l = len(arr2), len(arr2[0])

    arr3 = []
    # O(nml) -> O((10^2)^3) -> O(10^6) -> 백만
    for i in range(n):
        temp_arr3 = []
        for j in range(l):
            temp_arr3.append(sum([a1 * a2[j] for a1, a2 in zip(arr1[i], arr2)]))
        arr3.append(temp_arr3)

    return arr3