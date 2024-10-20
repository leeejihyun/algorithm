# 각 문자열을 두 글자씩 끊어 다중집합을 만드는 함수
def str2multiset(s):
    ms = {}
    # len(s) = N
    # O(N * 2 * 2) -> O(N) -> O(1,000)
    for i in range(len(s) - 1):
        c = s[i:i + 2]
        # 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다.
        if c.isalpha():
            # 대문자와 소문자의 차이는 무시하기 위해 모두 소문자로 저장한다.
            c = c.lower()
            if c in ms:
                ms[c] += 1
            else:
                ms[c] = 1
    return ms


def solution(str1, str2):
    # 각 문자열을 두 글자씩 끊어 다중집합을 만든다.
    # O(len(str1) + len(str2)) -> O(N) -> O(1,000)
    ms1 = str2multiset(str1)
    ms2 = str2multiset(str2)

    if len(ms1) == len(ms2) == 0:
        sim = 1
    else:
        # 교집합 구하기
        # O(min(len(ms1), len(ms2))) -> O(N) -> O(1,000)
        it = []
        if len(ms1) <= len(ms2):
            for k in ms1:
                if k in ms2:
                    it += [k] * min(ms1[k], ms2[k])
        else:
            for k in ms2:
                if k in ms1:
                    it += [k] * min(ms1[k], ms2[k])

        # 합집합 구하기
        # O(len(str1) + len(str2)) -> O(N) -> O(1,000)
        un = []
        for k in ms1:
            if k in ms2:
                un += [k] * max(ms1[k], ms2[k])
            else:
                un += [k] * ms1[k]
        for k in ms2:
            if k in ms1:
                continue
            else:
                un += [k] * ms2[k]

        # 자카드 유사도 계산
        sim = (len(it) / len(un))
    return int(sim * 65536)