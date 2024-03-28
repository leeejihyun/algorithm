# 입력받은 식량창고 개수 정수로 변환
n = int(input())
# print(n)

# 공백으로 구분된 각 식량창고에 저장된 식량 개수 k를 입력받아 정수 변환 후 배열로 생성
a = list(map(int, input().split()))
# print(a)

d = [0] * (n + 1)
last_i = 0
# DP (Bottom up)
for i in range(3, n+1):
  if last_i + 2 > i - 1:
    continue
  else:
    d[i] = d[i-1] + a[last_i + 2]
    last_i = last_i + 2
  if i == 3:
    if a[i-3] + a[i-1] < a[i-2]:
      last_i = i-2
      d[i] = a[i-2]
    else:
      last_i = i-1
      d[i] = a[i-3] + a[i-1]
  print(last_i, d[i])