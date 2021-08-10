# min max

tc = int(input())

for test in range(tc):
    n = int(input())
    num_lst = list(map(int, input().split()))
    min, max = num_lst[0], num_lst[0]
    for num in num_lst:
        if min > num:
            min = num
        if max < num:
            max = num
    print("#{} {}".format(test+1, max-min))