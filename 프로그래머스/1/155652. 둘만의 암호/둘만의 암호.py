import re
def solution(s, skip, index):
    tmp = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for i in list(skip):
        tmp = tmp.replace(i,"")
    for i in s:
        ans += tmp[(tmp.find(i) + index) % len(tmp)]
    return ans