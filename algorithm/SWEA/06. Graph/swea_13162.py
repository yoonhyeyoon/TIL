# 최소 신장 트리

def Union(a,b) :
    pa = Find(a)
    pb = Find(b)
    if pa != pb :
        parent[pb] = pa
    return

def Find(a) :
    if parent[a] == a : return a
    ret = Find(parent[a])
    parent[a] = ret
    return ret

for tc in range(1, T + 1) :
    V,E = map(int, input().split())
    edge_lst = []
    for _ in range(E):
        n1, n2, cost = map(int, input().split())
        edge_lst.append((cost, n1, n2))
    de = - 1
    # sort
    edge_lst.sort()
    # init
    parent = [i for i in range(V+1)]

    total = 0
    cnt = V + 1
    for edge in edge_lst :
        cost, a, b = edge
        if Find(a) == Find(b) : continue
        Union(a,b)
        total += cost
        cnt -= 1
        if cnt == 1 : break

    print("#{} {}".format(tc, total))