# N개의 수, N-1개의 연산자
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것 구하는 프로그램
import itertools

# 첫째 줄에 개수 N (2 <= N <= 11)
n = int(input())
# print(f"n: {n}")
# 둘째 줄에 수열 A_1, ..., A_N (1 <= A_i <= 100)
nums = []
for num in map(int, input().split()):
  nums.append(num)
# print(f"nums: {nums}")
# 합이 N-1인 4개의 정수, 차례대로 덧셈, 뺄셈, 곱셈, 나눗셈 개수
ops = []
input_ops_n = list(map(int, input().split()))
pos_ops = ['+', '-', '*', '/']
for i in range(4):
  o_n = input_ops_n[i]
  o = pos_ops[i]
  for _ in range(o_n):
    ops.append(o)
# print(f"ops: {ops}")

# 최댓값, 최솟값 갱신
min_v = 1000000000
max_v = -1000000000

def operate(l, r, o):
  if o == '+': 
    return l + r
  if o == '-': 
    return l - r
  if o == '*': 
    return l * r
  if o == '/':
    if l < 0:
      l = -l
      return -(l // r)
    else:
      return l // r
# print(operate(7, 3, '/'))
# print(operate(-7, 3, '/'))

pers = set(itertools.permutations(ops, n-1))
# print(f"pers: {pers}")
for p in pers:
  l = nums[0]
  for i in range(1, n):
    r = nums[i]
    o = p[i-1]
    l = operate(l, r, o)
  if l < min_v:
    min_v = l
  if l > max_v:
    max_v = l

# 첫째 줄에 최댓값 출력
print(max_v)

# 둘째 줄에 최솟값 출력
print(min_v)
