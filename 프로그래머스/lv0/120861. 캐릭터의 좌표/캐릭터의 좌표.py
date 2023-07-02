def solution(keyinput, board):
    col = board[0]
    row = board[1]
    x, y = 0, 0
    for i in keyinput:
        if i == "left" and x-1 >= -(col // 2):
            x -= 1
        elif i == "right" and x+1 <= (col // 2):
            x += 1
        elif i == "up" and y+1 <= (row // 2):
            y += 1
        elif i == "down" and y-1 >= -(row // 2):
            y -= 1
    return [x, y]