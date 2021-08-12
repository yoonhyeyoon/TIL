# 특별한 정렬

tc = int(input())

for test in range(1, tc+1):
    n = int(input())
    lst = list(map(int, input().split()))


    for i in range(n):
        for j in range(i, n):
            if i % 2:
                if lst[i] > lst[j]: # 작은 수
                    lst[i], lst[j] = lst[j], lst[i]
            else:
                if lst[i] < lst[j]: # 큰 수
                    lst[i], lst[j] = lst[j], lst[i]

    print("#{}".format(test), end=" ")
    print(*lst[:10])
