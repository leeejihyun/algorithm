def solution(food_times, k):
  time = 0
  while True:        
      for i in range(len(food_times)):
          if time >= k:
              if food_times[i] != 0:
                  return i+1
              # 다 돌았는데 없으면 -1
              elif time >= k + len(food_times):
                  return -1
              else:
                  continue
          if food_times[i] != 0:
              # 1초씩 넘어가며 -1씩 섭취
              food_times[i] -= 1
              time += 1

print(solution([3, 1, 2], 5))