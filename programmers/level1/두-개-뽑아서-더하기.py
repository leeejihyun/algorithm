from itertools import permutations

def solution(numbers):
    answer = []
    for i, j in list(permutations(numbers,2)):
        new_number = i + j
        if new_number not in answer:
            answer.append(new_number)
    return sorted(answer)
