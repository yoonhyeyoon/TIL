# GNS

T = int(input())

for tc in range(1, T+1):
    test, n = input().split()
    lst = list(input().split())
    n = int(n)

    str_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    base = []

    for v in str_num:
        for i in range(n):
            if v == lst[i]:
                base.append(v)

    print(test)
    print(*base)