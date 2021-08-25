# 회전

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    queue = [0] * 2000
    lst = list(map(int, input().split()))
    front, rear = 0, 0

    for i in range(n):
        queue[rear] = lst[i]
        rear += 1

    for j in range(m):
        ret = queue[front]
        queue[rear] = ret
        front += 1
        rear += 1

    print("#{} {}".format(tc, queue[front]))