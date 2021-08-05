# n,k 입력받기
n, k = map(int, input().split())

# 횟수 초기화
cnt = 0
# n이 1이 될 때까지 반복
while n != 1:
  ## n이 k로 나눠지면
  if n % k == 0:
    ### 2번 방법 사용하고 결과 n에 대입
    n //= k
    ### 횟수 추가
    cnt += 1
  ## n이 k로 안 나눠지면
  else:
    ### 1번 방법 사용하고 결과 n에 대입
    n -= 1
    ### 횟수 추가
    cnt += 1

# 횟수 return
print(cnt)