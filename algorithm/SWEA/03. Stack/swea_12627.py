# 그래프 경로

# import sys
# sys.stdin = open('input.txt', 'r')

def dfs(now):
    for next in range(1, v+1):
        if adj[now][next] == 1 and visited[next] != 1:
            visited[next] = 1
            dfs(next)
    return


T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    adj = [[0] * (v+1) for _ in range(v+1)]

    for i in range(e):
        p, c = map(int, input().split())
        adj[p][c] = 1

    s, g = map(int, input().split())

    # 방문 기록장 만들기
    visited = [0 for _ in range(v+1)]
    visited[s] = 1

    dfs(s)

    if visited[g]:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))




