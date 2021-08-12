# 어디에 단어가 들어갈 수 있을까

tc = int(input())

for test in range(1, tc+1):
    n, m = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(n)]

    base = [[0] * (n+2) for _ in range(n+2)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            base[i][j] = lst[i-1][j-1]

    result_r = 0
    for i in range(1, n+1):
        for j in range(1, n+2-m):
            print(j)
            if base[i][j-1] == 0 and base[i][j+m] == 0:
                cnt = 0
                for k in range(m):
                    if base[i][j+k] == 1:
                        cnt += 1
                if cnt == m:
                    result_r += 1

    result_c = 0
    for i in range(1, n + 1):
        for j in range(1, n + 2 - m):
            if base[j-1][i] == 0 and base[j+m][i] == 0:
                cnt = 0
                for k in range(m):
                    if base[j+k][i] == 1:
                        cnt += 1
                if cnt == m:
                    result_c += 1




    print("#{} {}".format(test, result_r+result_c))






