# 그리디 알고리즘

# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S
# 왼쪽에서부터 순서대로 연산
# 곱하기 혹은 더하기만 가능

# output : S 숫자 사이에 곱하기 혹은 더하기로 만들 수 있는 가장 큰 수

# 가장 크게 만드려면 무조건 곱하기
# 예외 : 0, 1은 무조건 더하기

# 입력받은 문자열 S를 정수로 변환해 리스트에 저장
s = list(map(int, list(input())))
# print(s)

answer = s[0]

# 만들어질 수 있는 가장 큰 수 출력
# time complexity: O(N)
# N: S의 길이
for x in s[1:]:
  answer = max(answer + x, answer * x)

print(answer)