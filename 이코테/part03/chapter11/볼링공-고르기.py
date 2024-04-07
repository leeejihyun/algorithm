# 조합
# 무게 같은 경우 제외
from itertools import combinations

# 입력받은 볼링공의 개수 N, 공의 최대 무게 M을 정수로 변환
n, m = map(int, input().split())
# 입력받은 각 볼링공의 무게 정수로 변환
weight = list(map(int, input().split()))

# 2개의 요소로 이루어진 모든 조합 생성
combs = list(combinations(range(1, n+1, 1), 2))
# print(combs)
answer = 0
weihgt = weight.insert(0, 0)
# print(weight)
# 생성된 조합 출력
for comb in combs:
  a, b = comb
  if weight[a] != weight[b]:
    answer += 1

print(answer)