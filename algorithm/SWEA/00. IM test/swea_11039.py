# 사각형 찾기

def is_garo(i, j):
    cnt = 0
    for k in range(j, n):
        if MAP[i][k] == 1:
            cnt += 1
    return cnt

def is_sero(i, j):
    cnt = 0
    for k in range(i, n):
        if MAP[k][j] == 1:
            cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]

    square = []

    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 1:
                square.append(is_garo(i, j) * is_sero(i, j))

    print("#{} {}".format(tc, max(square)))