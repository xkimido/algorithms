def solution(board):
    n = len(board)
    
    count = 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                safe = True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                        safe = False
                        break
                if safe:
                    count += 1
                
    return count