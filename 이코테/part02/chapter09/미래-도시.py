# 플로이드 워셜 알고리즘

# 1~N번까지의 회사(노드)
# 특정 회사끼리는 서로 도로(간선)를 통해 연결
# 양방향 가능
# 도로 연결되어있다면 cost는 무조건 1

# 현재 1번 회사에 위치
# 소개팅 상대의 K번 회사 방문
# X번 회사에 방문 예정
# 최소 시간 계산
# 만약 도달할 수 없다면 -1 출력
import sys
INF = int(1e9)

# 회사 개수 N, 경로의 개수 M 입력받기
n, m = map(int, input().split())
print(n, m)

# 2차원 리스트로 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
  # A에서 B로 가는 비용은 C라고 설정
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

# 소개팅 상대의 회사 K, 최종 방문 회사 X 입력받기
x, k = map(int, input().split())

# X - K 도로 존재하지 않으면, -1 출력
if (graph[x][k] == INF) and (graph[k][x] == INF):
  print(-1)
  sys.exit(0)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for i in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])
      
# X - K 도로 존재하면, 1번 출발 K번 도착의 최단거리 + K번 출발 X번 도착의 최단거리 출력
print(graph[1][k] + graph[k][x])