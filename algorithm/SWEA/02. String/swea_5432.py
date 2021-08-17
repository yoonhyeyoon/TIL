# 쇠막대기 자르기

T = int(input())

for tc in range(1, T+1):
    raser = input()
    n = len(raser)
    i = 0
    ans = 0
    open_cnt = 0
    while i < n:
        if i+1 < n and raser[i] == '(' and raser[i+1] == ')':
            i += 2
            ans += open_cnt
        elif raser[i] == '(':
            i += 1
            open_cnt += 1
        elif raser[i] == ')':
            i += 1
            open_cnt -= 1
            ans += 1
    print("#{} {}".format(tc, ans))
