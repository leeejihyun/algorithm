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
    idx = 0
    for doll in basket[:]:
        if doll == prior_doll:
            answer += 2
            prior_doll_idx = idx - 2
            if prior_doll_idx >= 0:
                prior_doll = basket[prior_doll_idx]
            else:
                prior_doll = 0
            del basket[idx]
            del basket[idx-1]
            idx -= 2
        else:
            prior_doll = doll
        idx += 1

    return answer
