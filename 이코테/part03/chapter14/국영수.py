# 도현이네 반의 학생 수 N이 주어짐
n = int(input())

# 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어짐
arr = []
for _ in range(n):
  data = input().split()
  arr.append((data[0], data[1], data[2], data[3]))

## 정렬
# 국어 점수가 감소하는 순서
# 국어 점수가 같으면 영어 점수가 증가하는 순서
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서
arr.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬 기준으로 학생의 이름 출력
for a in arr:
    print(a[0])
