# 그리디 알고리즘
# 뒤집기 : 연속된 하나 이상의 숫자

# 문자열 S 입력받기
s = input()
cnt_0, cnt_1 = 0, 0
temp_c = s[0]

# 1을 0으로 바꾸기
for c in s:
  if c == '1':
    if temp_c != c:
      temp_c = c
      cnt_0 += 1
  
# print(cnt_0)

# 0을 1로 바꾸기
for c in s:
  if c == '0':
    if temp_c != c:
      temp_c = c
      cnt_1 += 1

# print(cnt_0)

# output : 다솜이가 해야 하는 행동(뒤집기)의 최소 횟수
print(min(cnt_0, cnt_1))