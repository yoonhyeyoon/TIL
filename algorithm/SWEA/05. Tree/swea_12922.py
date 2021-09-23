# 이진탐색


def dfs(now):
    global cnt
    if now > n:
        return
    dfs(now*2)
    lst[now] = cnt
    cnt += 1
    dfs(now*2+1)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = [-1 for _ in range(n+1)]
    cnt = 1
    dfs(1)
    print("#{} {} {}".format(tc, lst[1], lst[n//2]))


