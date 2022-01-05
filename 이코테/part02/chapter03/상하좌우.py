# N 저장
n = int(input())

# plan 저장
plan = input().split()

# x, y 초기화
x, y = 1, 1

# direction에 따라 좌표 움직이기
# 단, 정사각형 공간을 벗어나는 움직임은 무시
for direction in plan:
  if direction == 'L':
    y -= 1
    if y < 1 or y > n:
      y += 1
  elif direction == 'R':
    y += 1
    if y < 1 or y > n:
      y -= 1
  elif direction == 'U':
    x -= 1
    if x < 1 or x > n:
      x += 1
  elif direction == 'D':
    x += 1
    if x < 1 or x > n:
      x -= 1

# 최종 x, y 출력
print(x, y)