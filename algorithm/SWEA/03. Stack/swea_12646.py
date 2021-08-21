# 할아버지가 남긴 땅

def is_exist(y1,x1,y2,x2):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            if MAP[y][x] == 0: return True

    return False

def get_sum(y1,x1,y2,x2) :
    sum = 0
    for y in range(y1,y2+1) :
        for x in range(x1,x2+1) :
            sum += MAP[y][x]

    return sum

N,M = map(int , input().split())
MAP = [
    list(map(int, input().split())) for _ in range(N)
]

max_sum = int(-21e8)
# 직사각형 잡기
for y1 in range(0,N):
    for x1 in range(0,M):
        # y1,x1
        for y2 in range(y1, N):
            for x2 in range(x1, M):
                # y2,x2
                check = is_exist(y1,x1,y2,x2)
                if check == False : # 0이 없음
                    ret = get_sum(y1,x1,y2,x2)
                    if max_sum < ret :
                        max_sum = ret

print(max_sum)