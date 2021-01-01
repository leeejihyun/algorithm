def solution(board, moves):
    basket = []
    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] != 0:
                basket.append(board[row][move-1])
                board[row][move-1] = 0
                break

    answer = 0
    prior_doll = 0
    for doll in basket[:]:
        if doll == prior_doll:
            answer += 2
            prior_doll_index = basket.index(doll) - 1
            if prior_doll_index >= 0:
                prior_doll = basket[prior_doll_index]
            else:
                prior_doll = 0
            basket.remove(doll)
            basket.remove(doll)
        else:
            prior_doll = doll
    return answer
