n = int(input())

houses = list(map(int, input().split()))
# 정렬 : O(NlogN)
houses.sort()

# 가운데만 탐색
if len(houses) % 2 == 1:
  mid = len(houses) // 2 - 1
  print(mid)
else:
  answer_1, answer_2 = 0, 0
  mid_1 = len(houses) // 2 - 1
  mid_2 = mid_1 + 1
  for house in houses:
    answer_1 += abs(houses[mid_1] - house)
    answer_2 += abs(houses[mid_2] - house)
  if answer_1 < answer_2:
    print(houses[mid_1])
  elif answer_1 > answer_2:
    print(houses[mid_2])
  else:
    if houses[mid_1] < houses[mid_2]:
      print(houses[mid_1])