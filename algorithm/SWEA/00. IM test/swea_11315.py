# 오목 판정

def win(MAP):
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 'o':
                for k in range(6):
                    cnt = 0
                    for s in range(5):
                        ni = i + di[k] * s
                        nj = j + dj[k] * s
                        if ni < 0 or nj < 0 or ni >= n or nj >= n : continue
                        if MAP[ni][nj] == '.' : continue
                        cnt += 1
                    if cnt == 5:
                        return 'YES'
    return 'NO'


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    MAP = [list(input()) for _ in range(n)]

    di = [-1, 1, 0, 0, -1, -1]
    dj = [0, 0, -1, 1, -1, 1]

    print("#{} {}".format(tc, win(MAP)))