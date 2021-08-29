# 떡 먹는 호랑이

d, k = map(int, input().split())

x, y = 0, 1
for _ in range(2, d):
    x, y = y, x+y
for a in range(1, 1000):
    if (k - (a*x)) % y == 0:
        print(a)
        print((k - (a*x)) // y)
        break