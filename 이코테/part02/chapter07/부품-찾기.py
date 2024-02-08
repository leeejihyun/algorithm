# 이진 탐색 함수
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return "yes"
    elif array[mid] > target:
      return binary_search(array, target, start, mid - 1)
    else:
      return binary_search(array, target, mid + 1, end)
  return "no"
# N을 정수로 변환
n = int(input())

# N개의 정수를 배열에 저장
array = list(map(int, input().split()))

# M을 정수로 변환
m = int(input())

# M개의 정수를 배열에 저장
request_array = list(map(int, input().split()))

'''
# 파이썬 라이브러리로 정렬 -> O(NlogN)
sorted_array = sorted(array)
'''
# 계수 정렬로 정렬 -> O(2N+K)
# O(1)
k = 1000000
# O(N)
k = max(array)

count = [0] * (k + 1)

# O(N)
for i in range(n):
  count[array[i]] = 1
print(count)

# O(K)
sorted_array = [i for i in range(k+1) if count[i] > 0]
print(sorted_array)
# sorted_array = []
# for i in range(k+1):
#   if count[i] > 0:
#     sorted_array.append(i)

# 이진탐색을 M번 반복 -> O(MlogN)
for i in range(m):
  target = request_array[i]
  # 이진 탐색해서 있으면 yes, 없으면 no 출력
  answer = binary_search(sorted_array, target, 0, n-1)
  print(answer, end=" ")