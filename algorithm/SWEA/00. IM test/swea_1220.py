# Magnetic

T = 10

for tc in range(1, T+1):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for j in range(n):
        down = 0
        for i in range(n):
            if MAP[i][j] == 1:
                down += 1
            elif MAP[i][j] == 2 and down != 0:
                cnt += 1
                down = 0
                
    print(cnt)