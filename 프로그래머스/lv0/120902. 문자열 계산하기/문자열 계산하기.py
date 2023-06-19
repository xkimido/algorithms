def solution(my_string):
    mystr = my_string.split()
    answer = int(mystr[0])
    for i in range(1, len(mystr)):
        if mystr[i] == "+":
            answer += int(mystr[i+1])
        elif mystr[i] == "-":
            answer -= int(mystr[i+1])
    return answer