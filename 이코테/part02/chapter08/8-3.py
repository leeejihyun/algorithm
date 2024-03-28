## 호출되는 함수 확인
d = [0] * 100

def pivo(x):
  print('f(' + str(x) + ')', end=' ')
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = pivo(x-1) + pivo(x-2)
  return d[x]

print(pivo(6))