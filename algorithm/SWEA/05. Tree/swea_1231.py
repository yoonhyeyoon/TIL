# 중위순회

def tree(n):
    if n:
        tree(left[n])
        print(vo[n], end="")
        tree(right[n])

T = 10

for tc in range(1, T+1):
    print("#{}".format(tc), end=" ")
    n = int(input())
    vo = [''] * (n + 1)
    left = [0] * (n + 1)
    right = [0] * (n + 1)
    for i in range(1, n+1):
        v = input().split()
        vo[i] = v[1]
        if len(v) > 2:
            left[i] = int(v[2])
        if len(v) > 3:
            right[i] = int(v[3])
    tree(1)
    print()