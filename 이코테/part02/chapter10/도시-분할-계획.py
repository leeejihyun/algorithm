# N개의 노드, M개의 간선, 무방향
# 크루스칼 알고리즘 -> 간선 유지비의 합을 최소로
# 유지비 1이상 -> 길은 최대한 없애는게 좋음. 최소신장트리 조건 확보
# 서로소 알고리즘 -> 집합 2개 확인
# 각 집합에 대한 크루스칼 알고리즘

# find parent
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]
  
# union parent
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a > b:
    parent[a] = b
  else:
    parent[b] = a
  
# 노드(집)의 개수 N, 간선(길))의 개수 M
n, m = map(int, input().split())

edges = []
result = 0

# M줄에 걸쳐 간선 정보가 A, B, C로 주어짐
# A번 집과 B번 집을 연결하는 길의 유지비가 C
for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))
  
# parent 초기화
parent = [i for i in range(n + 1)]

# 끊을 간선은 유지비가 가장 많이 드는 것으로 골라야 함. 따라서 내림차순 정렬
edges.sort(reverse=True)

for edge in edges:
  c, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    edges.remove(edge)
    break

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합:', end='')
for i in range(1, n + 1):
  print(find_parent(parent, i), end=' ')

print()