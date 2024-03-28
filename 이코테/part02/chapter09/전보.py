# 다익스트라 알고리즘
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C 입력받기
n, m, c = map(int, input().split())

# 통로 입력받기
vertices = [[] for _ in range(n+1)]
for _ in range(m):
  x, y, z = map(int, input().split())
  vertices[x].append((y, z))

# 최단 거리 저장하는 distance 초기화
distance = [INF] * (n+1)

# 다익스트라 알고리즘
def daikstra(start):
  q = []
  # start 노드 초기화
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    # 방문한 노드는 pass
    if distance[now] < dist:
      continue
    for y, z in vertices[now]:
      if dist + z < distance[y]:
        distance[y] = dist + z

# 다익스트라 알고리즘 시행
daikstra(c)

# 도시 C에서 보낸 메시지 받게 되는 도시의 총 개수
cnt = 0
# 도시들이 모두 메시지를 받는 데까지 걸리는 시간
max_dist = 0
for i in range(1, n+1):
  # INF면 count X
  if distance[i] == INF:
    continue
  cnt += 1
  if distance[i] > max_dist:
    max_dist = distance[i]

print(cnt, max_dist)