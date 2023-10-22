def solution(board, moves):
    answer = 0
    doll_list = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                continue
            else:
                doll_list.append(board[j][i-1])
                board[j][i-1] = 0
                if len(doll_list) > 1:
                    if doll_list[-1] == doll_list[-2]:
                        doll_list.pop(-1)
                        doll_list.pop(-1)
                        answer += 2
                break
    return answer