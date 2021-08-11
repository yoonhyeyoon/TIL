# Sum

tc = 10

for test in range(1, tc+1):
    case_num = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    a_total = 0
    b_total = 0
    max_num = int(-21e8)
    for i in range(100):
        x_total = 0
        y_total = 0


        a_total += lst[i][i]
        b_total += lst[i][100-1-i]

        for j in range(100):
            x_total += lst[i][j]
            y_total += lst[j][i]
        if max_num < x_total:
            max_num = x_total
        if max_num < y_total:
            max_num = y_total
    if max_num < a_total:
        max_num = a_total
    if max_num < b_total:
        max_num = b_total

    print("#{} {}".format(case_num, max_num))

