# 길찾기

def dfs(now):
    for next in range(100):
        if adj[now][next] == 1 and visited[next] == 0:
            visited[next] = 1
            dfs(next)

for T in range(1):
    tc, n = map(int, input().split())
    adj = [[0] * 100 for _ in range(100)]
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i+1]] = 1
    visited = [0 for _ in range(100)]
    visited[0] = 1

    dfs(0)
    print("#{} {}".format(tc, visited[-1]))