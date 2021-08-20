# 백만 장자 프로젝트

# 방법 1
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    is_sell = [False] * n

    # 사는 게 이득인 지 아닌 지 췍
    for i in range(n-1):
        for j in range(i+1, n):
            if cost[i] < cost[j]:
                is_sell[i] = True
                break

    buy_cost = 0
    buy_cnt = 0

    for i in range(n):
        if is_sell[i]:
            buy_cnt += 1
            buy_cost += cost[i]
        else:
            ans += (cost[i] * buy_cnt) - buy_cost # 판매수익 - 비용
            buy_cnt = 0
            buy_cost = 0
    
    print("#{} {}".format(tc, ans))

# 방법 2 반대로 풀기 
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cost = list(map(int, input().split()))

    maxi = cost[-1]
    ans = 0

    for i in range(n-1, -1, -1):
        if maxi > cost[i]:
            ans += maxi - cost[i]
        else:
            maxi = cost[i]
    print("#{} {}".format(tc, ans))
