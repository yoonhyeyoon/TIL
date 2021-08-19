# 종이붙이기

def func(n):
    if n == 10 : return 1
    if n == 20 : return 3

    a = func(n-10)
    b = func(n-20)

    return a + b * 2

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    print("#{} {}".format(tc, func(n)))
