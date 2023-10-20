def solution(numbers, hand):
    answer = ''
    lpos = [1,4] # means *
    rpos = [3,4] # means #
    for i in numbers:
        if i==1 or i==4 or i==7:
            answer+='L'
            lpos = [1,(i-1)/3+1]
        elif i==3 or i==6 or i==9:
            answer+='R'
            rpos = [3,i/3]

        else:
            if i==2: temp = [2,1]
            if i==5: temp = [2,2]
            if i==8: temp = [2,3]
            if i==0: temp = [2,4]
            ldis = abs(temp[0]-lpos[0])+abs(temp[1]-lpos[1])
            rdis = abs(temp[0]-rpos[0])+abs(temp[1]-rpos[1])
            if ldis<rdis:
                answer+='L'
                lpos = temp
            elif ldis>rdis:
                answer+='R'
                rpos =temp
            else:
                if hand == "right":
                    answer+='R'
                    rpos = temp
                else:
                    answer+='L'
                    lpos = temp
    return answer