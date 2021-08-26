# 미로의 거리

from collections import deque

def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    visited[sy][sx] = 0

    while queue:
        y, x = queue.popleft()
        if MAP[y][x] == 3:
            return visited[y][x]-1

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 > ny or 0 > nx or ny >= n or nx >= n : continue
            if visited[ny][nx] > 0 : continue
            if MAP[ny][nx] == 1 : continue
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))
    return 0

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    MAP = [list(map(int, input())) for _ in range(n)]

    dy = [-1, 1, 0, 0] # 위 아래 왼 오
    dx = [0, 0, -1, 1]

    visited = [[0] * n for _ in range(n)]


    for i in range(n): # 시작좌표 찾기
        for j in range(n):
            if MAP[i][j] == 2:
                sy = i
                sx = j


    print("#{} {}".format(tc, bfs(sy, sx)))