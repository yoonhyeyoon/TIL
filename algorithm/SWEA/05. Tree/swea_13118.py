# 전기버스 2

def dfs(now, cnt) :
    if now > N : # 고려 x
        return
    if visited[now] <= cnt : return # 백트래킹
    visited[now] = cnt
    if now == N :
        return
    # next = now + (1~lst[now])
    for dist in range(1,lst[now] + 1):
        dfs(now + dist , cnt + 1)
    return

T = int(input())

for tc in range(1, T + 1)  :
    lst = list(map(int ,input().split()))
    N = lst[0] # 종점
    visited = [999] * (N+1) # 탐색을 했을때 지금까지의 최소 교환횟수가 저장이 되어있다.
    dfs(1,0)

    print("#{} {}".format(tc, visited[N] - 1))