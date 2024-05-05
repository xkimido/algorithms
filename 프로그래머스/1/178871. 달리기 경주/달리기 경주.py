def solution(players, callings):
    answer = []

    p_dic = {player:i+1 for i,player in enumerate(players)}
    location_dic = {i+1:player for i,player in enumerate(players)}

    for c in callings:
        c_loc = p_dic[c]
        front = c_loc - 1
        front_p = location_dic[front]
        p_dic[c] -= 1
        p_dic[front_p] += 1
        location_dic[c_loc] = front_p
        location_dic[front] = c

    p_dic = dict(sorted(p_dic.items(),key=lambda x:x[1]))
    answer = list(p_dic.keys())

    return answer
