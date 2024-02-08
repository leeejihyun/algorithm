import sys

N, M = int(sys.argv[1]), int(sys.argv[2])
print(N, M)

graph = []
for i in range(3, len(sys.argv)):
    graph.append(sys.argv[i])

# 문자열로 받은 그래프 이중 리스트로 변환
new_graph = []
for i in range(N):
    row = graph[i]
    row_graph = [row[i] for i in range(len(row))]
    new_graph.append(row_graph)
print(new_graph)

# visited 초기화
# visited = [[False] * M] * N
visited = [[False] * M for i in range(N)]
stack = dict()
total_count = 0

def dfs(i, j, graph, visited):
    global total_count

    # 방문한 적 없는 노드만 방문
    if not visited[i][j]:
        visited[i][j] = True
        # print(visited)
        stack[(i,j)] = 0

        # 상하좌우 체크
        # 상
        if i > 0 and graph[i-1][j] == '0' and not visited[i-1][j]:
            dfs(i-1, j, graph, visited)
        # 하
        if i+1 < len(graph) and graph[i+1][j] == '0' and not visited[i+1][j]:
            dfs(i+1, j, graph, visited)
        # 좌
        if j > 0 and graph[i][j-1] == '0' and not visited[i][j-1]:
            dfs(i, j-1, graph, visited)
        # 우
        if j+1 < len(graph[0]) and graph[i][j+1] == '0' and not visited[i][j+1]:
            dfs(i, j+1, graph, visited)

        total_count += 1

for i in range(N):
    for j in range(M):
        dfs(i, j, new_graph, visited)

print(total_count)
# dfs(0, 0, new_graph, visited)
# for i, j in stack:
#     dfs(i, j, new_graph, visited)