# Time Complexity : O(N/2)
# Space Complexity : O(1) : half_len, n_left_sum, n_right_sum

# 입력받은 점수 N을 변수 선언 
n = input()

# 자릿수를 세서 절반을 나누기
half_len = int(len(n)/2)

# 왼쪽, 오른쪽 한 자리씩 parsing해서 더하기 (반복문/재귀 함수)
n_left_sum = 0
n_right_sum = 0
for i in range(half_len):
  n_left_sum += int(n[i])
  n_right_sum += int(n[i + half_len])

# 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 같다면 "LUCKY" 출력
if n_left_sum == n_right_sum:
  print("LUCKY")
# 다르면 "READY" 출력
else:
  print("READY")