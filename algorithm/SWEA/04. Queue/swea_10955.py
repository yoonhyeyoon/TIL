# 물놀이를 가자

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    MAP = [input() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    qu = deque()
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 'W':
                qu.append((i, j, 0))
                visited[i][j] = 1

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    cnt = 0
    ans = 0
    while qu:
        i, j, level = qu.popleft()
        for t in range(4):
            ni = i + di[t]
            nj = j + dj[t]
            if ni < 0 or nj < 0 or ni >= N or nj >= M : continue
            if MAP[ni][nj] == 'L' and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                qu.append((ni, nj, level+1))
                ans += level+1

    print("#{} {}".format(tc, ans))