from collections import deque

def bfs(graph, start, visited):
  answer = 0
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        answer += 1
        if answer == k:
          print(i)

# 입력받은 N, M, K, X 정수로 변경
n, m, k, x = map(int, input().split())
# print(n, m, k, x)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[] for _ in range(n+1)]

# M번 반복
for i in range(m):
  # 입력받은 A, B 정수로 변경
  a, b = map(int, input().split())
  graph[a].append(b)
print(graph)

visited = [False] * (n+1)
print(visited)

# distance = dict()
# for i in range(n):
#   distance[i+1] = 0
# print(distance)

# 최단거리 K인 도시 탐색
bfs(graph, x, visited)
# print(distance)
print(visited)
# k번 반복

# # 최단거리 K인 도시 번호 한줄씩 오름차순으로 출력
# for city in sorted(distance.keys()):
#   if distance[city] == k:
#     print(city)