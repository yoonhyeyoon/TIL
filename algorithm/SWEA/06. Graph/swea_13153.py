# ugly number

import heapq

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ugly = [0] * 1501
    th = 1
    minheap = []
    heapq.heappush(minheap, 1)  # 시작

    prev = - 1
    while th < 1501:
        now = heapq.heappop(minheap)
        if now == prev: continue

        ugly[th] = now
        th += 1
        # x2 x3 x5 -> minheap
        heapq.heappush(minheap, 2 * now)
        heapq.heappush(minheap, 3 * now)
        heapq.heappush(minheap, 5 * now)
        prev = now

    print('#{}'.format(tc), end=' ')
    for i in range(N):
        print(ugly[lst[i]], end=' ')
    print()