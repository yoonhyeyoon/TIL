# 시간복잡도 고려해주기
from collections import deque

def solution(prices):
    answer = []
    que = deque(prices)
    while que:
        q = que.popleft()
        count = 0
        for i in que:
            count += 1
            if i < q:
                break
        answer.append(count)
    return answer