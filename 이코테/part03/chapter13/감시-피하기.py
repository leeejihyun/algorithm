n = int(input())

teachers = []
data = []
for i in range(n):
  row = input().split()
  for j in range(n):
    if row[j] == 'T':
      teachers.append((i, j))
  data.append(row)
print(f'data : {data}')
print(f'teachers : {teachers}')

o_cnt = 3

answer = "NO"

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, data):
  global o_cnt
  while o_cnt != 0:
    temp_data = [row[:] for row in data]
    # temp_data[x][y] = 'O'
    print(f'temp_data : \n{temp_data[0]}\n{temp_data[1]}\n{temp_data[2]}\n{temp_data[3]}')
    # o_cnt -= 1
    
    # 선생님 개수만큼 돌기
    for tx, ty in teachers:
      # 장애물을 만날 때까지 반복
      for i in range(4):
        
        nx = tx + dx[i]
        ny = ty + dy[i]
        if nx < 0 or nx > n-1:
          continue
        if ny < 0 or ny > n-1:
          continue
        if temp_data[nx][ny] == 'S':
          return answer
        print(f'nx: {nx} / ny: {ny}')
        while temp_data[nx][ny] == 'X':
          nx += dx[i]
          ny += dy[i]
          if nx < 0 or nx > n-1:
            continue
          if ny < 0 or ny > n-1:
            continue
        dfs(nx, ny, temp_data)
  answer = "YES"
  return answer

dfs(0, 0, data)