def solution(survey, choices):
    scores = {"A":0, "N":0, "C":0, "F":0, "M":0, "J":0, "R":0, "T":0}
    for idx, choice in enumerate(choices):
        if choice - 4 > 0:
            scores[survey[idx][1]] += choice - 4
        elif choice - 4 < 0:
            scores[survey[idx][0]] += 4 - choice

    type = ""
    if scores["R"] >= scores["T"]:
        type += "R"
    else:
        type += "T"

    if scores["C"] >= scores["F"]:
        type += "C"
    else:
        type += "F"

    if scores["J"] >= scores["M"]:
        type += "J"
    else:
        type += "M"

    if scores["A"] >= scores["N"]:
        type += "A"
    else:
        type += "N"

    return type