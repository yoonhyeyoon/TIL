# 요리사

# 조합
import sys
sys.stdin = open("input.txt", "r")

def get_diff(used):
    A_sum = 0
    B_sum = 0
    for y in range(N):
        for x in range(y+1, N):
            if used[y] == 1 and used[x] == 1 :
                A_sum += MAP[y][x]
                A_sum += MAP[x][y]
            if used[y] == 0 and used[x] == 0 :
                B_sum += MAP[y][x]
                B_sum += MAP[x][y]
    return abs(A_sum - B_sum)

def dfs(level, prev):
    global min_diff
    if level == N/2:
        diff = get_diff(used)
        min_diff = min(min_diff, diff)
        return
    for i in range(prev + 1, N):
        used[i] = 1
        dfs(level + 1, i)
        used[i] = 0
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N
    min_diff = int(21e8)
    dfs(0, 0)
    print("#{} {}".format(tc, min_diff))
