import collections

collections.Counter('aaabbccccccddddd')
sample = collections.deque("hello")
sample.rotate(-1)
''.join(sample)

import collections

def solution(A, B):
    if A == B:
        return 0
    비교 = collections.deque(A)
    for i in range(len(A)):
        비교.rotate(1)
        if ''.join(비교) == B:
            return i + 1
    return -1

def solution(A, B):
    return (B*2).find(A)