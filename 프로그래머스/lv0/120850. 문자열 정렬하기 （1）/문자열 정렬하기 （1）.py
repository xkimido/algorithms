import re

def solution(my_string):
    # return sorted(list(re.sub('\D', '', my_string).replace('"', ''))) 실패
    # return sorted(re.findall('[0-9]', my_string)) 실패
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))