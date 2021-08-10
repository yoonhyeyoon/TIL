# gravity

n = int(input())
for num in range(n):
    N = int(input())
    lst = list(map(int, input().split()))
    result = 0
    for i in range(N-1):
        cnt = N-i-1
        for j in range(i+1, N-1):
            if lst[i] <= lst[j]:
                cnt -= 1
        if result < cnt:
            result = cnt
    print(f'#{num+1} {result}')

