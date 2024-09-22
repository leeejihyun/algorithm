INF = int(1e9)

n = int(input())
m = int(input())

# nxn 그래프 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

# 시작 도시와 도착 도시가 같은 경우 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    i, j, c = map(int, input().split())
    graph[i][j] = min(graph[i][j], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        # i에서 j로 갈 수 없는 경우 0 출력
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()