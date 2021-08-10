# Baby Gin

n = int(input())
for num in range(n):
    a = list(map(int, input().strip()))
    cnt = [0] * 10
    for val in a:
        cnt[val] += 1
    runn = 0
    triplet = 0
    i = 0
    while i < 10:
        if cnt[i] >= 3:
            cnt[i] -= 3
            triplet += 1
            continue
        if i < 8:
            if cnt[i] >= 1 and cnt[i + 1] >= 1 and cnt[i + 2] >= 1:
                runn += 1
                cnt[i] -= 1
                cnt[i + 1] -= 1
                cnt[i + 2] -= 1
                continue
        i += 1

    if runn + triplet == 2:
        print(f"#{num + 1} Baby Gin")
    else:
        print(f"#{num + 1} Lose")