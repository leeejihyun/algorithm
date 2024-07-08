n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값(median) 출력
print(data[(n-1) // 2])