# 최소 생산 비용

def dfs(level, sum):
    global min_sum
    if sum > min_sum : return # 백트래킹
    if level == N:
        min_sum = min(sum, min_sum)
        return
    for i in range(N):
        if used[i] == 1: continue
        used[i] = 1
        dfs(level + 1, sum + MAP[level][i])
        used[i] = 0
    return

T = int(input())

for tc in range(1, T + 1)  :
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_sum = int(21e8)
    dfs(0,0)
    print("#{} {}".format(tc, min_sum))