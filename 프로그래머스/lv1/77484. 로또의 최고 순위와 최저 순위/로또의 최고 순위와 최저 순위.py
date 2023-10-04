def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] # 딕셔너리 쓰지않고 순서대로 당첨 내용 리스트로!

    cnt_0 = lottos.count(0) # 찾고자 하는 항목이 파이썬의 리스트에 몇개나 들어있는지 확인하는 count 함수
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]