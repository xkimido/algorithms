del_list = ['~','!','@','#','$','%','^','&','*','(',')','=','+','[','{',']','}',':','?','<','>','/',","]
def solution(new_id):
    #소문자화
    id_lower = new_id.lower()
    #없어야 하는 것 삭제
    for pun in del_list:
        id_lower = id_lower.replace(pun, '')
    # 연속된 . 삭제하기
    temp = list(id_lower)
    temp_list = []
    # . 삭제할 위치 찾고 바꿔주기
    for i in range(len(temp)-1):
        if temp[i] == '.':
            if temp[i+1] =='.':
                temp_list.append(i)
            else:
                pass
    for i in temp_list:
        temp[i] = ''
    # 양 옆의 . 삭제
    id_2 = ''.join(temp)
    id_3 = id_2.strip('.')
    # 비어있다면 a 넣어주기
    if len(id_3) == 0:
        id_3 = 'a'
    else:
        pass
    # 길이 15 넘으면 줄이기
    if len(id_3) > 15:
        id_3 = id_3[:15]
    else:
        pass
    id_4 = id_3.strip('.')
    # 길이 3보다 작으면 바꿔주기
    if len(id_4) == 1:
        id_5 = id_4 *3
    elif len(id_4) == 2:
        id_5 = id_4 + id_4[-1]
    else:
        id_5 = id_4 
    return id_5