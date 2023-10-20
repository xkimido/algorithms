def solution(numbers, hand):
    answer = ''
    answer_list=[]
    keypad=[]
    keypad.append((4,2))
    for x in range(1,4):
        for y in range(1,4):
            keypad.append((x,y))
            
    left_x=4
    left_y=1
    right_x=4
    right_y=3
    
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]: 
            answer_list.append('L')
            left_x=keypad[numbers[i]][0]
            left_y=keypad[numbers[i]][1]
            
        elif numbers[i] in [3,6,9]:
            answer_list.append('R')
            right_x=keypad[numbers[i]][0]
            right_y=keypad[numbers[i]][1]
        else:
            dis_ri=abs(right_x-keypad[numbers[i]][0])+abs(right_y-keypad[numbers[i]][1])
            dis_le=abs(left_x-keypad[numbers[i]][0])+abs(left_y-keypad[numbers[i]][1])
            if dis_ri>dis_le:
                answer_list.append('L')
                left_x=keypad[numbers[i]][0]
                left_y=keypad[numbers[i]][1]
            elif dis_ri<dis_le:
                answer_list.append('R')
                right_x=keypad[numbers[i]][0]
                right_y=keypad[numbers[i]][1]
            else:
                if hand=='right':
                    answer_list.append('R')
                    right_x=keypad[numbers[i]][0]
                    right_y=keypad[numbers[i]][1]
                else:
                    answer_list.append('L')
                    left_x=keypad[numbers[i]][0]
                    left_y=keypad[numbers[i]][1]
        
                
    answer="".join(answer_list)            
    return answer  