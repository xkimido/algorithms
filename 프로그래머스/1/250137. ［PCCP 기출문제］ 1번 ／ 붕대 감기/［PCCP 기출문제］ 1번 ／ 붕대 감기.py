def solution(bandage, health, attacks):
    hp = health
    start = 1
    for i, j in attacks:
        hp += ((i - start) // bandage[0]) * bandage[2] + (i - start) * bandage[1]
        start = i + 1
        if hp >= health:
            hp = health
        hp -= j
        if hp <= 0:
            return -1
    return hp