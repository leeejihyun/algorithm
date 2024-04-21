import copy
import heapq

# 그래프 크기 입력받아 정수로 변환
n, k = map(int, input().split())
#print("n, k : ", n, k)

# 그래프 초기화
graph = []
q = []
new_q = []
for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] != 0:
      heapq.heappush(q, (data[j], i, j))
  graph.append(data)
#print("graph:", graph)
#print("priority queue:", q)
new_graph = copy.deepcopy(graph)

s, x, y = map(int, input().split())
#print("s, x, y : ", s, x, y)

# 상하좌우 정의
da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]

# 바이러스 증식
def grow(graph, a, b, virus):
  for i in range(len(da)):
    na = a + da[i]
    nb = b + db[i]
    if na < 0 or na > n-1 or nb < 0 or nb > n-1:
      continue
    if new_graph[na][nb] == 0:
      new_graph[na][nb] = virus
      heapq.heappush(new_q, (virus, na, nb))
  
time = 0
# s초 동안
while time < s:
  time += 1
  while q:
    virus, a, b = heapq.heappop(q)
    grow(graph, a, b, virus) # 바이러스 증식
    #print("priority queue:", q)
    #print("new_graph:", new_graph)
  q = copy.deepcopy(new_q)
  graph = copy.deepcopy(new_graph)

# s초 뒤에 바이러스 종류 출력 (없다면 0)
print(graph[x-1][y-1])