tc = int(input())

for test in range(1, tc+1):
    n = int(input())
    lst = list(map(int, input().split()))

    for i in range(n):
        for j in range(i, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


    print("#{}".format(test), end=" ")
    print(*lst)