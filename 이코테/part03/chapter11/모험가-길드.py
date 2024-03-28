# 입력받은 모험가의 수 N을 정수로 변환
n = int(input())

# 각 모험가의 공포도의 값을 정수로 변환해 배열 생성
array = list(map(int, input().split()))

# N개 길이를 가진 배열 생성
freq = [0] * (n + 1)

# 빈도수 계산
# Time complexity : O(N)
for a in array:
  freq[a] += 1
print(freq)

# Time complexity : O(N)
for i in range(1, n+1):
  if freq[i] != 0:
    freq[i]  = freq[i] // i
print(freq)

print(sum(freq))