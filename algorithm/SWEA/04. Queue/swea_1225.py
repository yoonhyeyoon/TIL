# 암호생성기

T = 10

for tc in range(1, T+1):
    t = int(input())
    lst = list(map(int, input().split()))
    queue = [0] * 200000
    front, rear = -1, -1

    for i in range(8):
        rear += 1
        queue[rear] = lst[i]

    i = 0
    while 1:
        i += 1

        front += 1
        ret = queue[front]
        rear += 1
        queue[rear] = ret-i

        i = i % 5

        if queue[rear] <= 0:
            queue[rear] = 0
            break


    print("#{}".format(t), end=" ")
    print(*queue[front+1:rear+1])