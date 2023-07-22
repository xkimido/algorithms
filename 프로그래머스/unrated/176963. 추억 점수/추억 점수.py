def solution(name, yearning, photo):
    result = []
    name_to_yearning = {n: y for n, y in zip(name, yearning)}

    for p in photo:
        total_yearning = 0
        for person in p:
            if person in name_to_yearning:
                total_yearning += name_to_yearning[person]
        result.append(total_yearning)

    return result