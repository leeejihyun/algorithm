# 입력받고 각 변수에 저장
N, M, K = map(int, input().split())

# 입력받고 배열 생성
array = list(map(int, input().split()))

array.sort()
maxNum = array[N-1] # 가장 큰 수 확인
nextMaxNum = array[N-2] # 두 번째로 큰 수 확인

answer = (maxNum * K + nextMaxNum) * (M // (K+1)) + maxNum * (M % (K+1))

print(answer)