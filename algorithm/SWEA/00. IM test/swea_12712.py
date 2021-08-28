# 파리퇴치3

def plus(MAP):
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    maxi = int(-21e8)
    for i in range(n):
        for j in range(n):
            total = 0
            total += MAP[i][j]
            for k in range(4):
                for d in range(1, m):
                    ni = i + di[k] * d
                    nj = j + dj[k] * d
                    if ni < 0 or nj < 0 or ni >= n or nj >= n : continue
                    total += MAP[ni][nj]
            if maxi < total:
                maxi = total
    return maxi

def multi(MAP):
    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]
    maxi = int(-21e8)
    for i in range(n):
        for j in range(n):
            total = 0
            total += MAP[i][j]
            for k in range(4):
                for d in range(1, m):
                    ni = i + di[k] * d
                    nj = j + dj[k] * d
                    if ni < 0 or nj < 0 or ni >= n or nj >= n : continue
                    total += MAP[ni][nj]
            if maxi < total:
                maxi = total
    return maxi


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]

    print("#{} {}".format(tc, max(plus(MAP), multi(MAP))))