# 창용 마을 무리의 개수

def find(a):
    if a == parent[a]:
        return a
    ret = find(parent[a])
    parent[a] = ret
    return ret

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa != pb:
        parent[pb] = pa
    return


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    group_cnt = N
    parent = [i for i in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        if find(a) != find(b):
            group_cnt -= 1
        union(a, b)

    print('#{} {}'.format(tc, group_cnt))