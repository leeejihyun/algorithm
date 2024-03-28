# 완전 탐색 : 가능한 모든 경우의 수를 고려
# 큰 단위로 자르면 더 짧게 압축되지 않는 예외 케이스?

# 시뮬레이션

def solution(s):
  # 가능한 최대 길이는 s의 길이
  answer = len(s)

  # answer 길이만큼 반복해서 자르기 -> O(1/N)
  ## 큰 단위로 자르면 더 짧게 압축되므로 큰 단위에서 작은거 찾으면 바로 return
  for i in reversed(range(1, len(s))):
    print(i)
    # 딕셔너리 생성
    s_dic = dict()
    j = 0
    while j < len(s):
      if s[j:j+i] in s_dic:
        s_dic[s[j:j+i]] += 1
      else:
        s_dic[s[j:j+i]] = 1
      j = j+i
    print(s_dic)
    # 딕셔너리 key + value 이어붙여 문자열 생성
    s_compressed = ''
    for k, v in s_dic.items():
      ## 단 1은 생략
      if v == 1:
          s_compressed +=  k
      else:
          s_compressed += str(v) + k
    print(s_compressed)
    # answer보다 길이가 작으면 answer 값 바로 return
    if len(s_compressed) < answer:
      print(answer)
      return answer
  print(answer)
  return answer

solution("aabbaccc")
# solution("ababcdcdababcdcd")
# solution("abcabcdede")
# solution("abcabcabcabcdededededede")
# solution("xababcdcdababcdcd")