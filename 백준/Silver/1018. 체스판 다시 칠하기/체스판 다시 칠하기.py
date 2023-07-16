def count_repaints(board, chessboard):
    repaints = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] != chessboard[i][j]:
                repaints += 1
    return repaints

def find_min_repaints(N, M, board):
    min_repaints = float('inf')
    chessboard1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
    
    chessboard2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                   ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                   ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
    
    for i in range(N - 7):
        for j in range(M - 7):
            sub_board = [row[j:j+8] for row in board[i:i+8]]
            repaints1 = count_repaints(sub_board, chessboard1)
            repaints2 = count_repaints(sub_board, chessboard2)
            min_repaints = min(min_repaints, repaints1, repaints2)
    
    return min_repaints

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    result = find_min_repaints(N, M, board)
    print(result)
