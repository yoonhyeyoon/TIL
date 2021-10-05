# 전자카트 

import sys
sys.stdin = open("input.txt", "r")

def dfs(now, cost, cnt):
    global min_cost
    if cnt == N:
        if adj[now][0] > 0:
            min_cost = min(min_cost, cost + adj[now][0])
        return

    for next in range(N):
        if adj[now][next] == 0: continue
        if visited[next] == 1: continue
        visited[next] = 1
        dfs(next, cost + adj[now][next], cnt + 1)
        visited[next] = 0

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    adj = [
        list(map(int, input().split())) for _ in range(N)
    ]
    visited = [0] * N

    min_cost = int(21e8)
    visited[0] = 1
    dfs(0,0,1)
    print("#{} {}".format(tc, min_cost))