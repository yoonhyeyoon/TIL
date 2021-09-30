# 이진수 표현

T = int(input())

for tc in range(1, T+ 1):
    N,M = map(int, input().split())

    new_M = M & ((1 << N) -1)
    de = -1
    if (1 << N) - 1 == new_M :
        print("#{} ON".format(tc))
    else :
        print("#{} OFF".format(tc))

# ---

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    light = list()
    ans = 'ON'
    while m:
        if m % 2:
            light.append(1)
        else:
            light.append(0)
        m //= 2
    if len(light) >= n:
        for i in range(n):
            if light[i] == 0:
                ans = 'OFF'
    else:
        ans = 'OFF'

    print("#{} {}".format(tc, ans))
