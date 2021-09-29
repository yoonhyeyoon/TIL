# 배달맨

from collections import deque

T = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, target):
    global sy
    global sx
    qu = deque()
    visited = [[0] * w for _ in range(h)]
    qu.append((y, x, 0))
    visited[y][x] = 1

    while qu:
        y, x, level = qu.popleft()
        if MAP[y][x] == target:
            sy = y
            sx = x
            return level # 시간
        for t in range(4):
            ny = y + dy[t]
            nx = x + dx[t]
            if ny < 0 or nx < 0 or ny >= h or nx >= w: continue
            if MAP[ny][nx] == '#': continue
            if visited[ny][nx] == 1: continue
            visited[ny][nx] = 1
            qu.append((ny, nx, level + 1))


for tc in range(1, T + 1):
    h, w, n = map(int, input().split())
    MAP = [list(input()) for _ in range(h)]
    sy = 0 # 숫자 있는 곳
    sx = 0
    total = 0
    for target in range(1, n+1):
        total += bfs(sy, sx, str(target))

    print("#{} {}".format(tc, total))
