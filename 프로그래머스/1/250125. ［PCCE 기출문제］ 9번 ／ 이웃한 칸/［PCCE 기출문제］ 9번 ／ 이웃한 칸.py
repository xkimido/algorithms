def solution(board, h, w):
    answer = 0
    
    if 0 < h:
        if board[h][w] == board[h-1][w]: answer += 1
    if 0 < w:
        if board[h][w] == board[h][w-1]: answer += 1
    if h < len(board) - 1:
        if board[h][w] == board[h+1][w]: answer += 1
    if w < len(board[0]) - 1:
        if board[h][w] == board[h][w+1]: answer += 1

    return answer