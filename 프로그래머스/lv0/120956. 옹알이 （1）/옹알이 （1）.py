import re

def solution(babbling):
    regex = re.compile('^(aya|ye|woo|ma)+$')
    return len([i for i in babbling if regex.match(i)])