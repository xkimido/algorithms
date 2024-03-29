from collections import deque


def solution(bandage, health, attacks):
    end = attacks[-1][0]
    attacks = deque(attacks)
    hp = health

    time = 0
    for t in range(1, end + 1):
        if health <= 0:
            return -1

        if not attacks:
            break
        time += 1
        if t == attacks[0][0]:
            health -= attacks.popleft()[1]
            time = 0

        elif time == bandage[0]:
            health += bandage[1] + bandage[2]
            time = 0

        else:
            health += bandage[1]

        if health > hp:
            health = hp

    return health if health > 0 else -1