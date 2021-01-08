def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = []
    for person in [person1, person2, person3]:
        cnt = 0
        j = 0
        for i in range(len(answers)):
            if person[j] == answers[i]:
                cnt += 1
            j += 1
            if j == len(person):
                j = 0
        count.append(cnt)
    
    max_cnt = max(count)
    answer = [idx + 1 for idx, value in enumerate(count) if value == max_cnt]
    
    return sorted(answer)
