# 위상 정렬
from collections import deque

# 입력 받은 노드 개수를 정수로 변환
n = int(input())

# 진입 차수 저장
indegree = [0] * (n + 1)

# 그래프 초기화
graph = [[] for i in range(n + 1)]

# 노드별 비용 리스트 초기화
cost = [0] * (n + 1)

# 최소 시간을 담은 비용 리스트 초기화
min_cost = [[] for i in range(n + 1)]

# 입력 받은 간선 정보를 그래프에 저장
for i in range(1, n + 1):
  line = list(map(int, input().split()))
  cost[i] = line[0]
  
  for j in line[1:-1]:
    graph[j].append(i)
    indegree[i] += 1

# print("graph:", graph)
# print("indegree:", indegree)
# print("cost:", cost)

def topology_sort():
  result = []
  q = deque()

  # 진입 차수가 없는 노드부터 시작
  for i in range(1, len(indegree)):
    if indegree[i] == 0:
      q.append(i)
  
  # 진입 차수가 없는 노드가 없을 때까지 반복
  while q:
    now = q.popleft()
    if min_cost[now]:
      min_cost[now] = [max(min_cost[now])]
    min_cost[now].append(cost[now])
    result.append(now)
    for i in graph[now]:
      indegree[i] -= 1
      min_cost[i].append(cost[now])
      if indegree[i] == 0:
        q.append(i)

  # print("min_cost:", min_cost)
  # N개의 강의에 대하여 수강하기까지 걸리는 최소 시간 각각 출력
  # print("result:", result)
  for i in result:
    print(sum(min_cost[i]))

topology_sort()