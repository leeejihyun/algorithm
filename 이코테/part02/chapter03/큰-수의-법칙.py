# 입력받고 각 변수에 저장
N, M, K = map(int, input().split())
# print(N, M, K)

# 입력받고 배열 생성
array = []
array = list(map(int, input().split()))
# print(array)

# 가장 큰 수 확인
maxNum = max(array)
# print(maxNum)

# 가장 큰 수가 몇 개 있는지 확인
maxNumArray = [i for i, j in enumerate(array) if j == maxNum]
# print(maxNumArray)

# 1개면 다음으로 큰 수 확인
answer = 0
cnt = 0
if len(maxNumArray) == 1:
	array.remove(maxNum)
	nextMaxNum = max(array)
	# print(nextMaxNum)
	while cnt < M:
		for j in range(K):
			answer += maxNum
			cnt += 1
		answer += nextMaxNum
		cnt += 1
else:
	answer = maxNum * M
print(answer)
