def solution(participant, completion):
    participant_dict = dict.fromkeys(participant, 0)
    completion_dict = dict.fromkeys(participant, 0)
    for p in participant:
        participant_dict[p] += 1
    for c in completion:
        completion_dict[c] += 1
    for key, value in completion_dict.items():
        if completion_dict[key] != participant_dict[key]:
            answer = key
            return answer
