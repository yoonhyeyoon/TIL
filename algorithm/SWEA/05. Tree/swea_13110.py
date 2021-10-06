# 병합정렬

def merge_sort(s, e):
    global cnt

    if s+1 == e: return

    # 분할
    mid = (s + e) // 2
    merge_sort(s, mid)
    merge_sort(mid, e)

    if lst[mid-1] > lst[e-1]:
        cnt += 1

    # 병합
    a = s
    b = mid
    t = s
    
    while a < mid and b < e:
        if lst[a] <= lst[b]:
            res[t] = lst[a]
            a += 1
            t += 1
        elif lst[b] < lst[a]:
            res[t] = lst[b]
            b += 1
            t += 1
    while a < mid:
        res[t] = lst[a]
        a += 1
        t += 1
    while b < e:
        res[t] = lst[b]
        b += 1
        t += 1
    for i in range(s,e):
        lst[i] = res[i]


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    res = [0] * n
    merge_sort(0, n)
    print("#{} {} {}".format(tc, res[n//2], cnt))