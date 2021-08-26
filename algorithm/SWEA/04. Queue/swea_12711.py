# 피자 굽기

from collections import deque

T = int(input())

for tc in range(1,T+1) :
    N,M = map(int, input().split())
    cheese = [-1]
    cheese += list(map(int,input().split()))
    oven = deque(range(1, N+1))

    num = N+1
    while len(oven) > 1:
        pizza_num = oven[0]
        cheese[pizza_num] //= 2
        if cheese[pizza_num] == 0:
            oven.popleft()
            if num <= M:
                oven.append(num)
                num += 1
        else:
            tmp = oven.popleft()
            oven.append(tmp)
    print("#{} {}".format(tc, oven[0]))