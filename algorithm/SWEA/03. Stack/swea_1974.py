# 스도쿠 검증

def is_same(MAP):
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            check = [0] * 10
            for y2 in range(y, y+3):
                for x2 in range(x, x+3):
                    if check[MAP[y2][x2]] == 0:
                        check[MAP[y2][x2]] += 1
                    else:
                        return 0
    return 1

def is_row(MAP):
    for y in range(9):
        check = [0] * 10
        for x in range(9):
            if check[MAP[y][x]] == 0:
                check[MAP[y][x]] += 1
            else:
                return 0
    return 1

def is_col(MAP):
    for x in range(9):
        check = [0] * 10
        for y in range(9):
            if check[MAP[y][x]] == 0:
                check[MAP[y][x]] += 1
            else:
                return 0
    return 1


T = int(input())

for tc in range(1, T+1):
    MAP = [list(map(int, input().split())) for _ in range(9)]

    if is_same(MAP) and is_row(MAP) and is_col(MAP):
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))