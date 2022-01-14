# 세로 크기 n, 가로 크기 m 저장
n, m = map(int, input().split())

# 게임 캐릭터가 있는 칸의 좌표 (a,b)와 바라보는 방향 d 저장
a, b, d = map(int, input().split())

# 2차원 배열 gameMap 생성
gameMap = []
# n행만큼 gameMap에 append
for i in range(n):
  gameMap.append(list(map(int, input().split())))

# 북동남서 direction 생성
direction = [0, 1, 2, 3]

# 움직일 수 있는 da, db 정의
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

# 가본 칸은 바다로 변경
gameMap[a][b] = 1

# 캐릭터가 방문한 칸의 수 cnt 생성
cnt = 1

# 회전 횟수 turnTime 생성
turnTime = 0

# 매뉴얼대로 움직이기
while True:
  # d 왼쪽으로 회전
  d = direction[direction.index(d) - 1]
  na = a + da[d]
  nb = b + db[d]
  # 바로 왼쪽 방향에 0이 있으면
  if gameMap[na][nb] == 0:
    # 가본 칸은 바다로 변경
    gameMap[a][b] = 1
    # 왼쪽 한칸 전진
    a, b = na, nb
    # cnt 추가
    cnt += 1
    turnTime = 0
    continue
  # 바로 왼쪽 방향에 0이 없으면
  else:
    turnTime += 1

  # 4번 반복 후에도 갈곳이 없다면
  if turnTime == 4:
    # 뒤로 한칸 후진
    na = a - db[d]
    nb = b - da[d]
    # 후진 할 수 있으면
    if gameMap[na][nb] == 0:
      a, b = na, nb
      # 가본 칸은 바다로 변경
      gameMap[a][b] = 1
      # cnt 추가
      cnt += 1
      # 1단계 다시 진행
      turnTime = 0
    # 후진 할 수 없으면 while문 빠져나오기
    else:
      break

# cnt 출력
print(cnt)