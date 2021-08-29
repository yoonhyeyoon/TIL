# Sum

T = 10

for tc in range(1, T+1):
    t = int(input())
    MAP = [list(map(int, input().split())) for _ in range(100)]
    total = []

    for i in range(100):    # 가로
        cnt = 0
        for j in range(100):
            cnt += MAP[i][j]
        total.append(cnt)

    for j in range(100):    # 세로
        cnt = 0
        for i in range(100):
            cnt += MAP[i][j]
        total.append(cnt)

    cnt = 0
    for i in range(100):    # 오른쪽 대각선
        cnt += MAP[i][i]
    total.append(cnt)

    cnt = 0
    for i in range(100):    # 왼쪽 대각선
        cnt += MAP[i][99-i]
    total.append(cnt)

    print("#{} {}".format(t, max(total)))