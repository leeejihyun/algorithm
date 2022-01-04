# n,k 입력받기
n, k = map(int, input().split())
# 횟수 초기화
cnt = 0

while True:
  ## n이 k로 나눠질 때까지 1씩 빼기
  target = (n // k) * k
  # n이 1일 때 반복문 탈출
  if n == 1:
    break
  cnt += (n - target)
  n = target
  ## k로 나누기
  cnt += 1
  n //= k

# 횟수 return
print(cnt)