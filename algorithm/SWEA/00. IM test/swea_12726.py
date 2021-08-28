# 토굴

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(n)]

    for k in range(1, m+1):
        for i in range(n):
            for j in range(n):
                if m % k == 0:
                    if MAP[i][j]:
                        MAP[i][j] = 0
                    else:
                        MAP[i][j] = 1
                elif (i+1 + j+1 == k) or (i+1 + j+1) % k == 0:
                    if MAP[i][j]:
                        MAP[i][j] = 0
                    else:
                        MAP[i][j] = 1
    ans = 0
    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 1:
                ans += 1
    print("#{} {}".format(tc, ans))