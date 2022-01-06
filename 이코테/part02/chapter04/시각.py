# 정수 N 저장
n = int(input())

if n >= 3:
  answer = (n+1)*6*10*6*10 - n*5*9*5*9
else:
  answer = (n+1)*6*10*6*10 - 5*9*5*9

# 3이 하나라도 포함되는 모든 경우의 수 answer 출력
print(answer)