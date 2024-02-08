# BFS와 다른 점
# graph가 인접 행렬이라 이중 리스트로 구현해야 한다는 점
# 연결 관계 없음.
# 0인지 1인지 봐서 1인 노드만 돌면 됨
# 그렇다고 1인 노드를 다 돌면 안되고 (n,m)까지 가기 위한 1인 노드만 돌아야 함

from collections import deque

# BFS 메서드 정의
def bfs(graph, sx, sy, visited):
  global answer
  queue = deque([(sx,sy)])
  # print(queue)
  # 현재 노드를 방문 처리
  visited[sx][sy] = True
  # 첫 칸은 무조건 1이므로 이동 칸에 추가
  answer += 1
  # 큐가 빌 때까지 반복
  while queue:
    print(queue)
    # 큐에서 하나의 원소를 뽑기
    (x, y) = queue.popleft()
    if (x, y) == (n-1, m-1):
      break
    # 상하좌우 1이면 큐에 추가
    if y+1 < m and graph[x][y+1] == 1 and not visited[x][y+1]:
      queue.append((x, y+1))
      visited[x][y+1] = True
      answer += 1
      continue
    if x+1 < n and graph[x+1][y] == 1 and not visited[x+1][y]:
      queue.append((x+1, y))
      visited[x+1][y] = True
      answer += 1
      continue
    if y-1 >= 0 and graph[x][y-1] == 1 and not visited[x][y-1]:
      queue.append((x, y-1))
      visited[x][y-1] = True
      answer += 1
      continue
    if x-1 >= 0 and graph[x-1][y] == 1 and not visited[x-1][y]:
      queue.append((x-1, y))
      visited[x-1][y] = True
      answer += 1
  

# 행, 열 개수 정수로 변환
n, m = map(int, input().split())
# print(n, m)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = []
for i in range(n):
  graph.append(list(map(int, input())))
# print(graph)

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = []
for i in range(n):
  visited.append([False] * m)
# print(visited)

answer = 0

# 정의된 BFS 함수 호출
bfs(graph, 0, 0, visited)

# 최소 이동 칸 수 출력
print(answer)