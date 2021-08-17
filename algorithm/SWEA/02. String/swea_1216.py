# 회문 2

T = 1

for tc in range(1, T+1):
    t = int(input())
    base = [list(input()) for _ in range(100)]
    maxi = 0
    for i in range(100):
        for j in range(100):
            lst = []
            for c in range(100):
                if j + c < 100:
                    lst.append(base[i][j+c])
                if lst == lst[::-1]:
                    if maxi < len(lst):
                        maxi = len(lst)

    for i in range(100):
        for j in range(100):
            lst = []
            for c in range(100):
                if i + c < 100:
                    lst.append(base[i+c][j])
                if lst == lst[::-1]:
                    if maxi < len(lst):
                        maxi = len(lst)

    print("#{} {}".format(tc, maxi))