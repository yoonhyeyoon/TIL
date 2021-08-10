# 숫자카드

tc = int(input())

for test in range(1, tc+1):
    n = int(input())
    lst = list(map(int, input().strip()))

    cnt_lst = [0] * 10

    for i in lst:
        cnt_lst[i] += 1

    max_n = int(-21e8)
    for i in range(len(cnt_lst)):
       if max_n <= cnt_lst[i]:
            max_n = cnt_lst[i]
            result = i
    print("#{} {} {}".format(test, result, max_n))