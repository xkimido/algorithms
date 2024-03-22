def solution(bandage, health, attacks):

    maxhealth = health
    maxtime = attacks[-1][0]
    attack_dict = {}
    for i in attacks:
        attack_dict[i[0]]=i[1]

    t=0

    continue_sec = 0

    while t<=maxtime:

        if t in attack_dict:
            health -= attack_dict[t]
            continue_sec=0

            if health <=0:
                return -1

        else:
            continue_sec += 1
            if continue_sec < bandage[0]:
                health += bandage[1]
                if health>maxhealth:
                    health = maxhealth

            else:
                health = health + bandage[1] + bandage[2]
                if health>maxhealth:
                    health = maxhealth
                continue_sec=0

        t+=1

    return health