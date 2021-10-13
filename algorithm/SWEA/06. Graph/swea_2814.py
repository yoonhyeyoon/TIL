# 최장 경로

def dfs(n, cnt):
    global ans
    if ans < cnt:
        ans = cnt
    for j in range(1, N + 1):
        if visited[j] == 0 and adj[n][j]:
            visited[j] = 1
            dfs(j, cnt + 1)
            visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    ans = 0
    for _ in range(M):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1
    for i in range(1, N + 1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0

    print('#{} {}'.format(tc, ans))