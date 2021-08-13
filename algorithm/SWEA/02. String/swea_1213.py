# 방법 1 

def is_pattern(start_idx, pn):
    if start_idx + pn -1 >= len(lst): return 0 # 인덱스 초과 방지
    for i in range(pn):
        # lst[start_idx + i] vs pattern[i]
        if lst[start_idx + i] != pattern[i]:
            return 0

    return 1

T = 10

for tc in range(1, T+1):
    tc = input()
    pattern = list(input().strip())
    lst = list(input().strip())


    cnt = 0
    for i in range(len(lst)):
        ret = is_pattern(i, len(pattern))
        if ret == 1:
            cnt += 1

    print("#{} {}".format(tc, cnt))

# 방법 2

    for start_idx in range(len(lst)-len(pattern)+1):
        for p_idx in range(len(pattern)):
            if lst[start_idx+p_idx] != pattern[p_idx]:
                break
        else:
            cnt += 1
