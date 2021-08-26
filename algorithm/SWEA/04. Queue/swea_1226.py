# 미로1

from collections import deque

def bfs(si, sj):

    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = 1

    while queue:
        x, y = queue.popleft()
        if MAP[x][y] == 3:
            return 1
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if nx < 0 or ny < 0 or nx >= 16 or ny >= 16 : continue
            if MAP[ny][nx] == 1 : continue
            if visited[ny][nx] == 1 : continue
            queue.append((ny, nx))
            visited[ny][nx] = 1
    return 0



T = 10

for i in range(1, T+1):
    n = int(input())
    MAP = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if MAP[i][j] == 2:
                si = i
                sj = j

    print("#{} {}".format(n, bfs(si, sj)))