# 사칙연산

import sys
sys.stdin = open('input.txt', 'r')


def dfs(now):
    if now > n:
        return
    if type(tree[now]) == int:
        return tree[now]

    a = dfs(left[now])
    b = dfs(right[now])

    if tree[now] == '+':
        return a + b
    elif tree[now] == '-':
        return a - b
    elif tree[now] == '*':
        return a * b
    elif tree[now] == '/':
        return a / b


T = 10

for tc in range(1, T + 1):
    n = int(input())
    tree = [0] * (n+1)
    left = [0] * (n+1)
    right = [0] * (n+1)

    for i in range(n):
        lst = input().split()
        if len(lst) == 2:
            tree[int(lst[0])] = int(lst[1])
        else:
            tree[int(lst[0])] = lst[1]
            left[int(lst[0])] = int(lst[2])
            right[int(lst[0])] = int(lst[3])

    ans = dfs(1)
    print('#{} {}'.format(tc, ans))







