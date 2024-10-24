from collections import deque


def solution(priorities, location):
    answer = 0
    n = len(priorities)

    # O(n)
    lp = [(l, p) for l, p in zip(range(n), priorities)]

    # 정렬 -> O(nlogn)
    slp = sorted(lp, key=lambda x: x[1])

    # O(n)
    q = deque(lp)

    # O(n) -> O(100)
    while q:
        # 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
        l, p = q.popleft()
        # 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
        if slp[-1][1] > priorities[l]:
            q.append((l, p))
            continue
        # 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
        # 3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
        else:
            slp.pop()
            answer += 1
            if l == location:
                return answer