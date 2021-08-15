# 손익분기점

A, B, C = map(int, input().split())

if A > 0 and C-B > 0:
    print(A // (C-B) + 1)
else:
    print(-1)