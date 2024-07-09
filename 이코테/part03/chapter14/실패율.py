def solution(N, stages):
  numerator = [0] * (N + 2)
  denominator = [0] * (N + 2)

  # O(len(stages) * (N + 1)) = O(200,000 * 501) = O(100,200,000) -> 1억
  for stage in stages:
      numerator[stage] += 1
      for prev_stage in range(1, stage + 1):
          denominator[prev_stage] += 1

  temp_answer = []
  # O(N) -> 500
  for i in range(1, N+1):
      if denominator[i] != 0:
          failure = numerator[i] / denominator[i]
      else:
          failure = 0
      temp_answer.append((i, failure))
  # 퀵 + 병합 정렬 : O(NlogN) -> 1,349
  temp_answer.sort(key=lambda x: (-x[1], x[0]))

  answer = [x[0] for x in temp_answer]
  return answer

print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])) #[3,4,2,1,5]
print(solution(4,	[4,4,4,4,4])) #[4,1,2,3]