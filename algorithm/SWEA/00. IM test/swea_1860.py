# 진기의 최고급 붕어빵

# 방법 1
T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    fish = [0] * 101
    ans = 'Possible'
    for i in range(m, 101):
        if i % m == 0:
            fish[i] = fish[i-1] + k
        else:
            fish[i] = fish[i-1]
    for i in range(n):
        if fish[p[i]] > 0:
            for j in range(p[i], 101):
                fish[j] -= 1
        else:
            ans = 'Impossible'

    print("#{} {}".format(tc, ans))

# 방법 2

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    person = list(map(int, input().split()))
    person.sort()
    ans = 'Possible'
    eat = 0
    for p in person:
        fish = p // m * k
        eat += 1
        if fish - eat >= 0:
            pass
        else:
            ans = 'Impossible'