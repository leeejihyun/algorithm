from string import ascii_uppercase

# 문자열 s 입력받기
s = input()

# 알파벳과 숫자 구분
# Time complexity : O(N)
# Space complexity : O(N)
a_list = [c for c in s if c.isalpha()]
n_list = [int(c) for c in s if c.isdigit()]

# 알파벳 오름차순 정렬
# 계수 정렬
# Time complexity : O(K + N)
# Space complexity : O(K)
# input : str / array
# ouput : str / array
a_str = ''
count = dict()
for c in ascii_uppercase:
  count[c] = 0
for i in range(len(a_list)):
  count[a_list[i]] += 1
for c in ascii_uppercase:
  for j in range(count[c]):
    a_str += c
# # 퀵 정렬(sorted)
# # Time complexity : O(NlogN)
# # Space complexity : O(1)
# a_list.sort()
# a_str = ''.join(a_list)

# 모든 숫자를 더한 값
n_sum = sum(n_list)
  
# 문자로 변환
n_sum_str = str(n_sum)

# a_sorted + n_sum 붙여 한 문자열로 만들기
print(a_str + n_sum_str)