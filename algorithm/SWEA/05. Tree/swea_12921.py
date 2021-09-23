# subtree

def dfs(now):
    global cnt
    if now == 0:
        return
    cnt += 1
    dfs(c[now][0])
    dfs(c[now][1])


T = int(input())
for tc in range(1, T+1):
    e, n = map(int, input().split())
    lst = list(map(int, input().split()))
    c = [[0,0] for _ in range(e+2)]
    for i in range(0, len(lst), 2):
        if c[lst[i]][0] == 0:
            c[lst[i]][0] = lst[i+1]
        else:
            c[lst[i]][1] = lst[i+1]
    cnt = 0
    dfs(n)
    print("#{} {}".format(tc, cnt))

