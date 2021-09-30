# 이진수2

T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    ans = ''

    while N:
        N *= 2

        if N >= 1:
            ans += '1'
            N -= 1
        else:
            ans += '0'
        if len(ans) > 12:
            ans = 'overflow'
            break

    print('#{} {}'.format(tc, ans))