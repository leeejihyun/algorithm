# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
a = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# DP 진행(보텀업)
d[0] = a[0]
d[1] = max(a[0], a[1])
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + a[i])

# 계산된 결과 출력
# print(d)
print(d[n-1])