# 색칠하기

tc = int(input())

for test in range(1, tc+1):
    n = int(input())
    base = [[''] * 10 for _ in range(10)]
    purple = 0

    for i in range(n):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if color == 1:
                    base[x][y] += str(color)
                elif color == 2:
                    base[x][y] += str(color)

    for i in range(10):
        for j in range(10):
            if base[i][j] == '12' or base[i][j] == '21':
                purple += 1
    print("#{} {}".format(test, purple))