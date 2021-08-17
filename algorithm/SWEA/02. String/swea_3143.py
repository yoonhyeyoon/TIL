# 가장 빠른 문자열 타이핑

def is_same(start, pattern):
    if start + pattern -1 >= len(str1) : return 0
    for p in range(pattern):
        if str1[start+p] != str2[p]:
            return 0
    else: return 1



T = int(input())

for tc in range(1, T+1):
    str1, str2 = input().split()
    n = len(str1)
    p = len(str2)
    i = 0
    cnt = 0
    while i < n:
        if is_same(i, p):
            i += p
            cnt += 1
        else:
            i += 1
            cnt += 1

    print("#{} {}".format(tc, cnt))