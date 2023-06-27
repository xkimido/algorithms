def solution(quiz):
    return ['O' if eval(i.split('=')[0]) == int(i.split('=')[1]) else 'X' for i in quiz]