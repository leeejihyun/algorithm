# n, m 입력받아 저장
n, m = map(int, input().split())

finalCard = 0
# 행 수 만큼 반복
for i in range(n):
  ## 행마다 cards에 append
  row = list(map(int, input().split()))
  ## minCard 계산
  minCard = min(row)
  ## finalCard 계산
  finalCard = max(finalCard, minCard)

# minCards에서 max 계산해서 return
print(finalCard)