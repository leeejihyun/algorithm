# input N 입력받기
n = int(input())

# 퀵 정렬
# time complexity : O(NlogN)
'''
# 학생 정보를 빈 리스트에 튜플 형태로 저장
array = []
for i in range(n):
  string = input()
  array.append((string.split()[0], int(string.split()[1])))

# 성적을 기준으로 오름차순 정렬
array = sorted(array, key=lambda x: x[1])
  
# 학생의 이름을 순서대로 출력
for name, _ in array:
  print(name, end=" ")
'''
# 계수 정렬
# time complexity : O(2K)
# 학생 정보를 딕셔너리 형태로 저장
dic = dict()
for i in range(n):
  string = input()
  name = string.split()[0]
  score = int(string.split()[1])
  if score in dic.keys():
    dic[score].append(name)
  else:
    dic[score] = [name]

count = [0] * (100 + 1)

for score in dic.keys():
  count[score] = dic[score]

print(count)

for i in range(len(count)):
  if count[i] == 0:
    continue
  print(" ".join(count[i]), end=" ")