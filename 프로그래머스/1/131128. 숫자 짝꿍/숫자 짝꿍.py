def solution(X, Y):
    answer = ''
    d = {}
    x = [i for i in X]
    y = [i for i in Y]

    for i in range(9,-1,-1) :    
        if x.count(str(i)) >= y.count(str(i)) :
            d[i] = y.count(str(i))
        else :
            d[i] = x.count(str(i))
    if sum(d.values()) == 0: 
        return '-1'

    for key,value in d.items() :
        if value != 0 :
            answer += str(key)*value

    if answer[0] == '0' :
        return '0'

    return answer