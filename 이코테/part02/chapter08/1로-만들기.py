# 탑다운, 메모이제이션
# 재귀함수

# 입력받은 x를 정수로 변환
x = int(input())

# 연속적이지 않은 경우이므로 사전으로 구현
m_dict = dict()
m_dict[1] = 0

min_count = x

# 재귀함수
def getMinCount(x):
  # 이미 계산한 적 있는 문제라면 그대로 반환
  if x in m_dict.keys():
    return m_dict[x]
  # 아직 계산하지 않은 문제라면 결과 반환
  m_dict[x] = 0
  # 4가지 연산을 반복
  if x % 5 == 0:
    m_dict[x] += getMinCount(x//5)
    m_dict[x] += 1
    return m_dict[x]
  if x % 3 == 0:
    m_dict[x] += getMinCount(x//3)
    m_dict[x] += 1
    return m_dict[x]
  if x % 2 == 0:
    m_dict[x] += getMinCount(x//2)
    m_dict[x] += 1
    return m_dict[x]
  m_dict[x] += getMinCount(x-1)
  m_dict[x] += 1
  return m_dict[x]

print(getMinCount(x))