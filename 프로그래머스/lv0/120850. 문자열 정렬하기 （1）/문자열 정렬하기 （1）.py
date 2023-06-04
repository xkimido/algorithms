import re

def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))