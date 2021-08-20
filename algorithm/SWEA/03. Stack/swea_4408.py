# 자기 방으로 돌아가기

# 복도 값
def div(num):
    return (int(num)+1) // 2

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    students = [list(map(div, input().split())) for _ in range(n)]

    road = [0] * 201

    for i in range(n):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]
        for j in range(students[i][0], students[i][1]+1): # 현재방에서 목표방까지
            road[j] += 1

    maxi = 0 # 최대 필요시간
    for i in range(201):
        if maxi < road[i]:
            maxi = road[i]

    print("#{} {}".format(tc, maxi))