# 입력받은 N, M 모두 정수 변환
n, m = map(int, input().split())

# 입력받은 화폐의 가치를 정수로 변환해 array에 저장
array = []
for i in range(n):
  array.append(int(input()))
array.sort(reverse=True)

answer = 0
def getMinNum(m, array):
  global answer
  for a in array:
    if m // a == 0:
      continue
    if m % a == 0:
      answer += m // a
      return answer
    else:
      answer += 1
      return getMinNum(m % a, array)
  return -1

print(getMinNum(m, array))