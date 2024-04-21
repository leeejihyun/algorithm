def balance2correct(w):
  # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
  if w == '':
      return w
  # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
  count = {"(": 0, ")": 0}
  count[w[0]] += 1
  for i in range(1, len(w)):
      count[w[i]] += 1
      if count['('] == count[')']:
          break
  u = w[:i+1]
  v = w[i+1:]
  # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  if isCorrect(u):
      s = balance2correct(v)
      # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
      return u + s
  # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  else:
      #4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
      #4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
      #4-3. ')'를 다시 붙입니다. 
      s = balance2correct(v)
      s = '(' + s + ')'
      #4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
      if len(u) > 2:
          s = s + u[1:-1][::-1]
      else:
          u = ''
      #4-5. 생성된 문자열을 반환합니다.
      return s

# 올바른 괄호 문자열인지 확인
def isCorrect(p):
  stack = []
  for char in p:
      if char == ')':
          top_element = stack.pop() if stack else '#'
          if top_element != '(':
              return False
      else:
          stack.append(char)
  return not stack

def solution(p):
  # 만약 p가 이미 "올바른 괄호 문자열"이라면 그대로 return
  if isCorrect(p):
      answer = p
  # 아니라면 "균형잡힌 괄호 문자열" p를 "올바른 괄호 문자열"로 변환
  else:
      answer = balance2correct(p)
  return answer