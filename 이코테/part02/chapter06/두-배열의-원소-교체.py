# N, K 공백 구분해서 parsing 후 정수로 변환
input_string = input().split()
n, k = int(input_string[0]), int(input_string[1])
# print(n, k)

# 배열 A, B 공백 구분해서 parsing 후 정수로 변환, 리스트에 저장
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# print(a)
# print(b)

# time complexity: O(NlogN + K)
# A, B 퀵 정렬
a.sort()
b.sort(reverse=True)
'''pivot = 0
left = pivot + 1
right = len(n) - 1
while a[pivot] <= a[left] and left <= len(n) - 1:
  left += 1
while a[pivot] >= a[right] and right > pivot:
  right -= 1
if left > right:
  a[pivot], a[right] = a[right], a[pivot]
a[left], a[right] = a[right], a[left]
'''

# k번 바꿔치기
for i in range(k):
  if a[i] < b[i]:
    a[i] = b[i]
  else:
    break
'''
# time complexity: O(N*K)
# A의 최소값이 B의 최대값보다 작으면 바꿔치기
for i in range(k):
  if min(a) < max(b):
    min_index = a.index(min(a))
    a[min_index] = max(b)
    b.remove(max(b))
'''

# A 원소의 합 출력
# print(a)
print(sum(a))