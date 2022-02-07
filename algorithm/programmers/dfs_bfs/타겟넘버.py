# bfs
from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = deque()
    queue.append((numbers[0], 0))
    queue.append((-1 * numbers[0], 0))
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append((temp + numbers[idx], idx))
            queue.append((temp - numbers[idx], idx))
        else:
            if temp == target:
                answer += 1
    return answer

# dfs
answer = 0
def dfs(temp, idx, numbers, target):
    global answer
    n = len(numbers)
    if n == idx:
        if temp == target:
            answer += 1
            return
        else:
            return
    dfs(temp+numbers[idx], idx+1, numbers, target)
    dfs(temp-numbers[idx], idx+1, numbers, target)
def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer