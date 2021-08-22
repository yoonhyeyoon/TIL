# 숫자 배열 회전 

# 방법 1 함수
def rotate(MAP):
    temp = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            temp[x][n-1-y] = MAP[y][x]
    for y in range(n):
        for x in range(n):
            MAP[y][x] = temp[y][x]
    return temp


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    MAP = [list(input().split()) for _ in range(n)]
    do90 = rotate(MAP)
    do180 = rotate(MAP)
    do270 = rotate(MAP)

    print("#{}".format(tc))
    for i in range(n):
        print("{} {} {}".format(''.join(do90[i]), ''.join(do180[i]), ''.join(do270[i])))

# 방법 2 인덱스
    do90 = []
    do180 = []
    do270 = []

    for j in range(n):
        string = ""
        for i in range(n-1, -1, -1):
            string += MAP[i][j]
        do90.append(string)

    for i in range(n-1, -1, -1):
        string = ""
        for j in range(n-1, -1, -1):
            string += MAP[i][j]
        do180.append(string)

    for j in range(n-1, -1, -1):
        string = ""
        for i in range(n):
            string += MAP[i][j]
        do270.append(string)