def solution(answers):
    number_one = []
    number_two = []
    number_three = []
    answer = []
    for i in range(len(answers)):
        number_one.append((i+1)%5 or 5)
        if (i+1) % 2:
            number_two.append(2)
        elif (i+1) % 8 == 2:
            number_two.append(1)
        elif (i+1) % 8 == 4:
            number_two.append(3)
        elif (i+1) % 8 == 6:
            number_two.append(4)
        elif not (i+1)%8:
            number_two.append(5)
        if (i+1) % 10 == 1 or (i+1) % 10 == 2:
            number_three.append(3)
        elif (i+1) % 10 == 3 or (i+1) % 10 == 4:
            number_three.append(1)
        elif (i+1) % 10 == 5 or (i+1) % 10 == 6:
            number_three.append(2)
        elif (i+1) % 10 == 7 or (i+1) % 10 == 8:
            number_three.append(4)
        elif (i+1) % 10 == 9 or (i+1) % 10 == 0:
            number_three.append(5)
    correct_one,correct_two,correct_three = 0,0,0
    for i in range(len(answers)):
        if answers[i] == number_one[i]:
            correct_one += 1 
        if answers[i] == number_two[i]:
            correct_two += 1 
        if answers[i] == number_three[i]:
            correct_three += 1
    correct = [correct_one, correct_two, correct_three]
    if max(correct) == correct_one:
        answer.append(1)
    if max(correct) == correct_two:
        answer.append(2)
    if max(correct) == correct_three:
        answer.append(3)
    answer.sort()
    return answer