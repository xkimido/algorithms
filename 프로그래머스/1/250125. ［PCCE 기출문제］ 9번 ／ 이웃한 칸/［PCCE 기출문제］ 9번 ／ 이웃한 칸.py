def solution(board, h, w):
    answer = 0
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for x, y in moves:
        dx, dy = h + x, w + y
        if 0 <= dx < len(board) and 0 <= dy < len(board[0]):
            if board[dx][dy] == board[h][w]:
                answer += 1
    return answer