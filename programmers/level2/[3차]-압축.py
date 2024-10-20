def solution(msg):
    answer = []

    # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다. -> O(1)
    # key: 길이가 1인 모든 단어 / value: 색인 번호
    words = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {words[i]: i + 1 for i in range(len(words))}

    # O(N * N) -> O(N^2) -> O(1,000,000)
    # 최악의 경우는 1000글자이면서 사전에서 모두 1글자인 문자로 이루어진 경우
    while msg:
        # 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
        # 가장 큰 길이의 문자열부터 탐색, 찾을 때까지 반복 -> O(N) -> O(1,000)
        for l in range(len(msg), 0, -1):
            if msg[:l] in d:
                w = msg[:l]
                break

        # 3. w에 해당하는 사전의 색인 번호를 출력
        answer.append(d[w])

        # 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
        if l == len(msg):
            break
        c = msg[l]
        if not (w + c) in d:
            d[w + c] = len(d) + 1

        # 입력에서 w를 제거
        msg = msg[l:]
        # 5. 단계 2로 돌아간다.
    return answer