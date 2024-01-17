def solution(s):
    l = len(s)
    try:
        a = int(s)
        if l == 4 or l == 6:
            return True
        else:
            return False
    except:
        return False