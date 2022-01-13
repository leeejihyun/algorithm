# 나이트의 위치 location 저장
location = input()

# location을 row와 col로 분리
col = ord(location[0]) - ord('a') + 1
row = int(location[1])

# 나이트가 이동할 수 있는 8가지 steps 선언
steps = [(-2,-1), (-2,1), (2,-1), (2,1), (1,2), (1,-2), (-1,2), (-1,-2)]

# 나이트가 이동할 수 있는지 카운트 선언
cnt = 0

# steps에 따라 이동
for step in steps:
  newRow = row + step[0]
  newCol = col + step[1]
  ## 해당 위치로 이동 가능하면 카운트 증가
  if newRow >= 1 and newRow < 8 and newCol >= 1 and newCol < 8:
    cnt += 1

# cnt 출력
print(cnt)