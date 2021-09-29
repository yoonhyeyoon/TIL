# 바이러스

from collections import deque

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    qu = deque()
    qu.append((y, x))
    visited[y][x] = 1

    while qu:
        y, x = qu.popleft()

        for t in range(4):
            ny = y + dy[t]
            nx = x + dx[t]
            if ny < 0 or nx < 0 or ny >= n or nx >= m: continue
            if MAP[ny][nx] == 0: continue
            if visited[ny][nx] == 1: continue
            visited[ny][nx] = 1
            qu.append((ny, nx))


for tc in range(1, T + 1):
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and MAP[i][j] == 2:
                bfs(i, j)
                cnt += 1
    print("#{} {}".format(tc, cnt))