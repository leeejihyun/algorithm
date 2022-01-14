# 세로 크기 n, 가로 크기 m 저장
n, m = map(int, input().split())

# 게임 캐릭터가 있는 칸의 좌표 (a,b)와 바라보는 방향 d 저장
a, b, d = map(int, input().split())

# 캐릭터가 방문한 칸의 수 cnt 생성
cnt = 0

# 육지인지 바다인지에 대한 정보 sea 저장
# 2차원 배열 gameMap 생성
gameMap = []
# 한줄한줄 받아서 gameMap에 append
while True:
  line = input()
  if not line:
    break
  line = list(map(int, line.split()))
  gameMap.append(line)

# 동서남북 direction 생성
direction = [0, 1, 2, 3]

# 움직일 수 있는 da, db 정의
da = [0, -1, 0, 1]
db = [-1, 0, 1, 0]

# 가본 칸은 바다로 변경, cnt 추가
gameMap[a][b] = 1
cnt += 1

# 매뉴얼대로 움직이기
while True:
  # 4번동안 반복
  i = 0
  while i < 4:
    newA = a + da[d]
    newB = b + db[d]
    # 바로 왼쪽 방향에 0이 있으면
    if gameMap[newA][newB] == 0:
      # d 왼쪽으로 회전
      d = direction[direction.index(d) - 1]
      # 왼쪽 한칸 전진
      a, b = newA, newB
      # 가본 칸은 바다로 변경, cnt 추가
      gameMap[a][b] = 1
      cnt += 1
      i = 0
    # 바로 왼쪽 방향에 0이 없으면
    else:
      # d 왼쪽으로 회전
      d = direction[direction.index(d) - 1]
      i += 1

  # 4번 반복 후에도 갈곳이 없다면 뒤로 한칸 후진
  newA = a - db[d]
  newB = b - da[d]
  # 후진 할 수 있으면
  if gameMap[newA][newB] == 0:
    # 1단계 다시 진행
    a, b = newA, newB
    # 가본 칸은 바다로 변경, cnt 추가
    gameMap[a][b] = 1
    cnt += 1
  # 후진 할 수 없으면 while문 빠져나오기
  else:
    break

# cnt 출력
print(cnt)