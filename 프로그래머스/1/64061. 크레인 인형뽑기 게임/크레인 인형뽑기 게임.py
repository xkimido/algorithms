def solution(board, moves):
    box = []
    answer = 0
    for x in moves:
        for y in range(len(board)):
            if board[y][x-1]:
                if box and board[y][x-1] == box[-1]:
                    answer += 2
                    box.pop()
                    board[y][x - 1] = 0
                    break
                else:
                    box.append(board[y][x-1])
                    board[y][x - 1] = 0
                    break

    return answer