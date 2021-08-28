# 퍼펙트 셔플

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    card = input().split()
    ans = []
    if n % 2:
        for i in range(n // 2 + 1):
            ans.append(card[i])
            if n//2+1 + i < n:
                ans.append(card[n//2+1 + i])
    else:
        for i in range(n // 2):
            ans.append(card[i])
            ans.append(card[n//2 + i])

    print("#{} ".format(tc), end="")
    print(*ans)