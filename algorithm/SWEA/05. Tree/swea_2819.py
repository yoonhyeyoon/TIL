# 격자판의 숫자 이어 붙이기

import sys
sys.stdin = open("input.txt", "r")

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(i, j, line):
    if len(line) == 7:
        ans.add(line)
        return
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if ni < 0 or nj < 0 or ni >= 4 or nj >= 4: continue
        dfs(ni, nj, line+MAP[ni][nj])

T = int(input())

for tc in range(1, T+1):
    MAP = [list(input().split()) for _ in range(4)]
    ans = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, MAP[i][j])
    print("#{} {}".format(tc, len(ans)))