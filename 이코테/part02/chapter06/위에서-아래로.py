# input N 받기
n = int(input())
# print(n)

# input 수열 받기
array = []
for i in range(n):
  array.append(int(input()))
# print(array)

# 내림차순 정렬
count = [0] * (max(array) + 1)

for i in range(len(array)):
  count[array[i]] += 1
# print(count)

for i in range(len(count)-1, 0, -1):
  for j in range(count[i]):
    print(i, end=" ")
