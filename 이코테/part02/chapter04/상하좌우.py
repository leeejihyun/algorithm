# N 저장
n = int(input())

# plans 저장
plans = input().split()

# x, y 초기화
x, y = 1, 1

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveTypes = ['L', 'R', 'U', 'D']

# plan에 따라 좌표 움직이기
for plan in plans:
  for i in range(len(moveTypes)):
    if plan == moveTypes[i]:
      nx = x + dx[i]
      ny = y + dy[i]
      # 단, 정사각형 공간을 벗어나는 움직임은 무시
      if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
      # 이동 수행
      x, y = nx, ny

# 최종 x, y 출력
print(x, y)
