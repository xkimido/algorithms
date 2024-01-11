def solution(s):
    arr= s.split(" ")
    answer_list = []
    for i in range(len(arr)):
        temp = arr[i]
        temp_list = list(map(str,temp))
        for j in range(len(temp_list)):
            if j % 2 == 0:
                temp_list[j] = temp_list[j].upper()
            else:
                temp_list[j] = temp_list[j].lower()
        item = "".join(temp_list)
        answer_list.append(item)

    answer = " ".join(answer_list)
    return answer