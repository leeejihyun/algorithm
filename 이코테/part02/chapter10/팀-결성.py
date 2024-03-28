# 테
    parents[b_p] = a_p

# N : 최대 번호
# M : 수행할 수 있는 연산의 개수
n, m = map(int, input().split())

# parents 초기화
parents = [i for i in range(n + 1)]

for _ in range(m):
  o, a, b = map(int, input().split())
  if o == 0:
    union(parents, a, b)
  elif o == 1:
    if findParent(parents, a) == findParent(parents, b):
      print("YES")
    else:
      print("NO")