def solution(skill, skill_trees):
    answer = 0

    skills = set(skill)

    # 가능한 순서만 집합에 추가
    # O(26)
    orders = set()
    for i in range(len(skill), 0, -1):
        orders.add(skill[:i])

    # skill_trees 돌면서 skill에 있는 스킬만 추출
    # O(20 x 26) -> O(520)
    for s in skill_trees:
        o = ""
        for c in s:
            if c in skills:
                o += c
        # 가능한 순서라면 answer += 1
        if (o in orders) or (not o):
            answer += 1

    return answer