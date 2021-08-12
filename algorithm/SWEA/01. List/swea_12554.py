# 이진탐색 대결 

tc = int(input())

for test in range(1, tc+1):
    left = 1
    p, a_key, b_key = map(int, input().split())
    a_cnt, b_cnt = 0, 0
    right = p
    # binary search
    while left <= right:
        a_cnt += 1
        mid = (left + right) // 2
        if a_key == mid:
            break
        if a_key < mid:
            right = mid
        elif mid < a_key:
            left = mid

    left = 1
    right = p
    while left <= right:
        b_cnt += 1
        mid = (left + right) // 2
        if b_key == mid:
            break
        if b_key < mid:
            right = mid
        elif mid < b_key:
            left = mid
