# 파스칼의 삼각형 

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    print("#{}".format(tc))
    lst = [[0] * n for n in range(1, n+1)]

    for i in range(n):
        for j in range(len(lst[i])):
            if j == 0:
                lst[i][j] = 1
            if i >= 1:
                if 0 < j < len(lst[i]) -1:
                    lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
                else:
                    lst[i][j] = lst[i-1][j-1]
    for l in range(len(lst)):
        print(*lst[l])

# 방법 2 DP
    for i in range(n):
        lst[i][0] = 1
        lst[i][i] = 1
    for y in range(2, n):
        for x in range(1, y):
            lst[y][x] = lst[y-1][x-1] + lst[y-1][x]