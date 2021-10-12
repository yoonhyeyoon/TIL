# 정사각형 방

## 방법 1 - 메모이제이션
import sys
sys.stdin = open("text.txt", "r")

T = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]
def dfs(y,x):
    if memo[y][x] > 0 : # memo 가 기록 되어 있을때  return
        return memo[y][x]

    max_ret = 1
    for t in range(4) :
        ny = y + dy[t]
        nx = x + dx[t]
        if ny < 0 or nx < 0 or ny >= N or nx >= N : continue
        if MAP[y][x] + 1 != MAP[ny][nx] : continue
        ret = dfs(ny,nx) + 1 # ny,nx ~ 의 경로길이 + 현재 경로길이
        max_ret = max(max_ret, ret)

    memo[y][x] = max_ret # 현재 정답을 기록
    return max_ret

for tc in range(1,T+1) :
    N = int(input())
    MAP = [
        list(map(int ,input().split())) for _ in range(N)
    ]
    memo = [
        [0] * N for _ in range(N)
    ]
    max_length = 0
    min_num = int(21e8)
    for y in range(N):
        for x in range(N) :
            length = dfs(y,x) # [y][x]에서 출발해서 얻어오는 길이
            # length vs max_length
            if length >= max_length :
                max_length = length
                if length == max_length :
                    min_num = min(min_num , MAP[y][x])
                else : # 클때는 무조건 갱신한다.
                    min_num = MAP[y][x]

    print("#{} {} {}".format(tc, min_num, max_length))


## 방법2 - 연속된 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def count(have):
    global min_cnt, start_idx
    cnt = 1
    start = 0
    for i in range(len(have)):
        if have[i] == 1:
            cnt += 1
            if start > 0 : continue
            start = i
        else:
            if cnt > 1:
                if min_cnt > cnt:
                    min_cnt = cnt
                    start_idx = start
            start = 0
            cnt = 1
    return

def have_check(y, x):
    for t in range(4):
        ny = y + dy[t]
        nx = x + dx[t]
        if ny < 0 or nx < 0 or ny >= N or nx >= N : continue
        if MAP[y][x] + 1 != MAP[ny][nx] : continue
        have[MAP[y][x]] = 1
        have_check(ny, nx)
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    have = [0] * (N*N)
    for i in range(N):
        for j in range(N):
            have_check(i, j)
    cnt = 0
    min_cnt = int(21e8)
    start_idx = 0
    count(have)
    print("#{} {} {}".format(tc, start_idx, min_cnt))