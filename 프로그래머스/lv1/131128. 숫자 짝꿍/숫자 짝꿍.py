from functools import reduce
import re
def solution(X, Y):
    result = "".join(sorted(reduce(lambda result, i: result + i*min(X.count(i), Y.count(i)), map(str, range(10)), ""), reverse=True)) or "-1"
    return "0" if re.match(r"0+", result) else result