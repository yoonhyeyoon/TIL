# 이진 트리 전위 순회

def dfs(now):
    if now == 0 : return
    preorder.append(now)
    dfs(left[now])
    dfs(right[now])
    return

T = int(input())

for tc in range(1,T+1):
    K = int(input())
    left = [0 for _ in range(20)]
    right = [0 for _ in range(20)]

    for _ in range(K-1) :
        parent, child = map(int,input().split())
        if left[parent] == 0:
            left[parent] = child
        else :
            right[parent] = child

    preorder = []
    dfs(1)

    print("#{}".format(tc),end = ' ')
    print(*preorder)