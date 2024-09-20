n, m = map(int, input().split())

array_1d = list(map(int, input().split()))
array_2d = []
i = 0
for _ in range(n):
  array_2d.append(array_1d[i:i+m])
  i += m

gold_dict = {}

def mine(x, y, n, m):
  if x >= n or y >= m:
    return 0
  if (x, y) in gold_dict.keys():
    return gold_dict[(x, y)]
  gold_dict[(x, y)] = array_2d[x][y]
  dx = [-1, 0, 1]
  dy = [1, 1, 1]
  max_gold_sum = -1
  for i in range(3):
    nx, ny = x + dx[i], y + dy[i]
    if nx < 0 or nx >= n or ny >= m:
      continue
    gold_sum = mine(nx, ny, n, m)
    if gold_sum > max_gold_sum:
      max_gold_sum = gold_sum
  if max_gold_sum == -1:
    return 0
  gold_dict[(x, y)] += max_gold_sum
  return gold_dict[(x, y)]

max_gold_sum = -1
for i in range(n):
  gold_sum = mine(i, 0, n, m)
  if gold_sum > max_gold_sum:
    max_gold_sum = gold_sum
print(max_gold_sum)