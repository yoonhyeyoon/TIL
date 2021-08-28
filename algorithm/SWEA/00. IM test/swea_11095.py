# 타일 로봇

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    MAP = [[0] * 10 for _ in range(10)]
    for _ in range(n):
        y1, x1, y2, x2 = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                MAP[y][x] = 1

    ans = 0
    for i in range(10):
        for j in range(10):
            if MAP[i][j] == 1:
                ans += 1

    print("#{} {}".format(tc, ans))