# n, m 입력받아 저장
n, m = map(int, input().split())

# cards 배열 생성
cards = []
# 행 수 만큼 반복
for i in range(n):
  ## 행마다 cards에 append
  cards.append(list(map(int, input().split())))

#minCards 배열 생성
minCards = []
# 행마다 반복
for row in cards:
  ## minCard 계산
  minCard = min(row)
  ## minCards에 append
  minCards.append(minCard)

# minCards에서 max 계산해서 return
print(max(minCards))