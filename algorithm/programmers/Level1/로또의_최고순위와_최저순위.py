def solution(lottos, win_nums):

    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
            lottos.remove(x)
    return rank[cnt_0 + ans],rank[ans]