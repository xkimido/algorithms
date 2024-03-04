def solution(board, h, w):
    dy = [0,-1,0,1]
    dx = [-1,0,1,0]
    answer = 0
    
    for i in range(4):
        nh = h + dy[i]
        nw = w + dx[i]
        if 0<= nh < len(board) and 0<= nw < len(board[0]):
            if board[nh][nw] == board[h][w]:
                answer += 1
    
    return answer