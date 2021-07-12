def solution(array, commands):
    answer = []
    
    # commands에서 command 꺼내오기
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        # 1. array에서 i번째부터 j번째까지 자르기
        new_array = array[i-1:j]

        # 2. 1에서 나온 배열 정렬
        new_array.sort()

        # 3. 2에서 나온 배열의 k번째 숫자 추출하여 answer에 담기
        answer.append(new_array[k-1])
    
    return answer
